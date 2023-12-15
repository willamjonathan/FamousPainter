from deap import tools
from deap import algorithms

def ElitismFunct(pop, toolbox, cross_prob, mutation_prob, num_gen, callback=None, the_statistic=None,
             best_indiv=None, verbose=__debug__):
    # pop: The pop of individuals.
    # toolbox: A toolbox containing methods for genetic operators (selection, crossover, mutation, etc.).
    # cross_prob: Crossover probability.
    # mutation_prob: Mutation probability.
    # num_gen: Number of generations.
    # callback: A callback function that is called after each iteration.
    # the_statistic: Statistics object for collecting data during evolution.
    # best_indiv: An object to store the best individuals and implement elitism.
    # verbose: A flag to control whether to print log information.
    logbook = tools.Logbook()
    logbook.header = ['gen', 'nevals'] + (the_statistic.fields if the_statistic else [])

    # check the individual with invalid fitness then used toolbox to assigned the fitness
    inv_individual = [ind for ind in pop if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, inv_individual)
    for ind, fit in zip(inv_individual, fitnesses):
        ind.fitness.values = fit

    if best_indiv is None:
        raise ValueError("best_indiv parameter must not be empty!")

    best_indiv.update(pop)
    hof_size = len(best_indiv.items) if best_indiv.items else 0

    record = the_statistic.compile(pop) if the_statistic else {}
    logbook.record(gen=0, nevals=len(inv_individual), **record)
    if verbose:
        print(logbook.stream)

    # start the generation process
    for gen in range(1, num_gen + 1):

        # selecting the next generation
        offspring = toolbox.select(pop, len(pop) - hof_size)

        # varying the pool of individuals
        offspring = algorithms.varAnd(offspring, toolbox, cross_prob, mutation_prob)

         # check the individual with invalid fitness then used toolbox to assigned the fitness
        inv_individual = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, inv_individual)
        for ind, fit in zip(inv_individual, fitnesses):
            ind.fitness.values = fit

        # add the best back to pop:
        offspring.extend(best_indiv.items)

        # update the best individual from the last generation
        best_indiv.update(offspring)

        pop[:] = offspring

        # insert the current generation statistics to the logbook
        record = the_statistic.compile(pop) if the_statistic else {}
        logbook.record(gen=gen, nevals=len(inv_individual), **record)
        if verbose:
            print(logbook.stream)

        if callback:
            callback(gen, best_indiv.items[0])

    return pop, logbook
