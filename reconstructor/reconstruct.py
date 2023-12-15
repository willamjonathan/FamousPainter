from deap import base
from deap import creator
from deap import tools

import random
import numpy
import os

import test_img
import elitism

import matplotlib.pyplot as plt
import seaborn as sns


file_path = "reconstructor/config.txt"
file_content = None
try:
    with open(file_path, "r") as file:
        file_content = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

print(file_content)


POLY_SIZE = 3
NUM_OF_POLYS = 100

BESTIND_SIZE = 20
POP_SIZE = 200
CROWDING = 10.0  
PROBABILITY_CROSSOVER = 0.9 
PROBABILITY_MUTATION = 0.5  
# MAX_GEN = 5000
# for testing purpose
MAX_GEN = 50


# calling the class for construction
img_upload = file_content
ConstructImage = test_img.ConstructImage(img_upload, POLY_SIZE)

# calc total params in chrom, each poly contains x,y 3 color value, and one alph value
NUM_OF_PARAMS = NUM_OF_POLYS * (POLY_SIZE * 2 + 4)

# parameters are on lowest 0 and highest 1
border_bottom, border_high = 0.0, 1.0 

toolbox = base.Toolbox()

# minimize fitness strategy
#make individual based on list
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Generate random floats within a given range for each dimension
# Parameters: low - lower bound, up - upper bound, num_of_params - number of dimensions
def randomFloat(low, up):
    return [random.uniform(l, u) for l, u in zip([low] * NUM_OF_PARAMS, [up] * NUM_OF_PARAMS)]

# make operator that able to produce random number of float
toolbox.register("attrFloat", randomFloat, border_bottom, border_high)

# make operator to fill indiv instance
toolbox.register("individualCreator",
                tools.initIterate,
                creator.Individual,
                toolbox.attrFloat)

# make operator to make list of individual
toolbox.register("popCreator",
                tools.initRepeat,
                list,
                toolbox.individualCreator)


# this is for the fitness calculation 
def getDiff(individual):
    return ConstructImage.MSE_diff(individual, "MSE"),

toolbox.register("evaluate", getDiff)


# the operator for genetic
toolbox.register("select", tools.selTournament, tournsize=2)

toolbox.register("mate",
                tools.cxSimulatedBinaryBounded,
                low=border_bottom,
                up=border_high,
                eta=CROWDING)

toolbox.register("mutate",
                tools.mutPolynomialBounded,
                low=border_bottom,
                up=border_high,
                eta=CROWDING,
                indpb=1.0/NUM_OF_PARAMS)


# saving the best drawing per 10 draw
def saveImage(gen, polyData):

    if gen % 10 == 0:

        folder = "reconstructor/images/results".format(POLY_SIZE, NUM_OF_POLYS)
        if not os.path.exists(folder):
            os.makedirs(folder)

        ConstructImage.save_img(polyData,
                            "{}/after-{}-gen.png".format(folder, gen),
                            "After {} Generations".format(gen))

# THE GENETIC ALGORITHM
def main():

    # initial population
    pop = toolbox.popCreator(n=POP_SIZE)

    # the statistic object
    the_statistic = tools.Statistics(lambda ind: ind.fitness.values)
    the_statistic.register("min", numpy.min)
    the_statistic.register("avg", numpy.mean)

    #  for the best individual size
    best_ind = tools.HallOfFame(BESTIND_SIZE)


    # do genetic algo  flow with elitism and it will save the image everytime it callbacks
    pop, logbook = elitism.ElitismFunct(pop,
                                                    toolbox,
                                                    cross_prob=PROBABILITY_CROSSOVER,
                                                    mutation_prob=PROBABILITY_MUTATION,
                                                    num_gen=MAX_GEN,
                                                    callback=saveImage,
                                                    the_statistic=the_statistic,
                                                    best_indiv=best_ind,
                                                    verbose=True)

    best = best_ind.items[0]
    print("Best solution result = ", best)
    print("Best score result = ", best.fitness.values[0])

    # draw best image next to reference image:
    ConstructImage.plt_img(ConstructImage.polyDataToImage(best))

    # extract statistics:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    sns.set_style("whitegrid")
    plt.figure("the_statistic:")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('n generation')
    plt.ylabel('Min / Average Fitness')
    plt.title('Min and Average fitness over Generations')
    plt.show()

if __name__ == "__main__":
    main()

