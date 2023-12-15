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
# problem related constants
POLY_SIZE = 3
NUM_OF_POLYS = 100

# calculate total number of params in chromosome:
# For each POLY we have:
# two coordinates per vertex, 3 color values, one alpha value
NUM_OF_PARAMS = NUM_OF_POLYS * (POLY_SIZE * 2 + 4)

# Genetic Algorithm constants:
pop_SIZE = 200
P_CROSSOVER = 0.9  # probability for crossover
P_MUTATION = 0.5   # probability for mutating an individual
MAX_GENERATIONS = 5000
BESTIND_SIZE = 20
CROWDING_FACTOR = 10.0  # crowding factor for crossover and mutation

# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# create the image test class instance:
img_upload = file_content
ConstructImage = test_img.ConstructImage(img_upload, POLY_SIZE)

# calculate total number of params in chromosome:
# For each POLY we have:
# two coordinates per vertex, 3 color values, one alpha value
NUM_OF_PARAMS = NUM_OF_POLYS * (POLY_SIZE * 2 + 4)

# all parameter values are bound between 0 and 1, later to be expanded:
BOUNDS_LOW, BOUNDS_HIGH = 0.0, 1.0  # boundaries for all dimensions

toolbox = base.Toolbox()

# define a single objective, minimizing fitness strategy:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMin)

# helper function for creating random real numbers uniformly distributed within a given range [low, up]
# it assumes that the range is the same for every dimension
def randomFloat(low, up):
    return [random.uniform(l, u) for l, u in zip([low] * NUM_OF_PARAMS, [up] * NUM_OF_PARAMS)]

# create an operator that randomly returns a float in the desired range:
toolbox.register("attrFloat", randomFloat, BOUNDS_LOW, BOUNDS_HIGH)

# create an operator that fills up an Individual instance:
toolbox.register("individualCreator",
                tools.initIterate,
                creator.Individual,
                toolbox.attrFloat)

# create an operator that generates a list of individuals:
toolbox.register("popCreator",
                tools.initRepeat,
                list,
                toolbox.individualCreator)


# fitness calculation using MSE as difference metric:
def getDiff(individual):
    return ConstructImage.MSE_diff(individual, "MSE"),

toolbox.register("evaluate", getDiff)


# genetic operators:
toolbox.register("select", tools.selTournament, tournsize=2)

toolbox.register("mate",
                tools.cxSimulatedBinaryBounded,
                low=BOUNDS_LOW,
                up=BOUNDS_HIGH,
                eta=CROWDING_FACTOR)

toolbox.register("mutate",
                tools.mutPolynomialBounded,
                low=BOUNDS_LOW,
                up=BOUNDS_HIGH,
                eta=CROWDING_FACTOR,
                indpb=1.0/NUM_OF_PARAMS)


# save the best current drawing every 100 generations (used as a callback):
def saveImage(gen, polyData):

    # only every 10 generations:
    if gen % 10 == 0:

        # create folder if does not exist:
        folder = "reconstructor/images/results".format(POLY_SIZE, NUM_OF_POLYS)
        if not os.path.exists(folder):
            os.makedirs(folder)

        # save the image in the folder:
        ConstructImage.save_img(polyData,
                            "{}/after-{}-gen.png".format(folder, gen),
                            "After {} Generations".format(gen))

# Genetic Algorithm flow:
def main():

    # create initial pop (generation 0):
    pop = toolbox.popCreator(n=pop_SIZE)

    # prepare the statistics object:
    the_statistic = tools.Statistics(lambda ind: ind.fitness.values)
    the_statistic.register("min", numpy.min)
    the_statistic.register("avg", numpy.mean)

    # define the hall-of-fame object:
    best_ind = tools.HallOfFame(BESTIND_SIZE)


    # perform the Genetic Algorithm flow with elitism and 'saveImage' callback:
    pop, logbook = elitism.ElitismFunct(pop,
                                                    toolbox,
                                                    cross_prob=P_CROSSOVER,
                                                    mutation_prob=P_MUTATION,
                                                    num_gen=MAX_GENERATIONS,
                                                    callback=saveImage,
                                                    the_statistic=the_statistic,
                                                    best_indiv=best_ind,
                                                    verbose=True)
    # generated()

    # print best solution found:
    best = best_ind.items[0]
    print()
    print("Best Solution = ", best)
    print("Best Score = ", best.fitness.values[0])
    print()

    # draw best image next to reference image:
    ConstructImage.plt_img(ConstructImage.POLYDataToImage(best))

    # extract statistics:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    # plot statistics:
    sns.set_style("whitegrid")
    plt.figure("the_statistic:")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Min / Average Fitness')
    plt.title('Min and Average fitness over Generations')

    # show both plots:
    plt.show()

        


if __name__ == "__main__":
    main()

