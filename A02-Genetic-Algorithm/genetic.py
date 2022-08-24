import math
def objective_function(individual):
    x = individual["x"]
    y = individual["y"]
    return math.sin(math.sqrt(x ** 2 + y ** 2))

def sort_population_by_fitness(population):
    return sorted(population, key=objective_function)

def select_individual(sorted_population, fitness_sum):
#     #write your code here
#     print("sp", sorted_population)
#     print("fs", fitness_sum)
    accum = 0
    for ind in sorted_population:
#         if ind['x'] < 0:
#             ind['y'] -= ind['x']
#             ind['x'] = 0

#         if ind['y'] < 0:
#             ind['x'] -= ind['y']
#             ind['y'] = 0

        r = random.uniform(0, fitness_sum) #RANDOM NUMBER ADD IN
        if accum > fitness_sum :
            return ind
        else :
            accum += r #objective_function(ind)


    #solve for new fitness sum
    #for each individual
    return individual


def crossover(individual_a, individual_b):
    ### write your code here
    new_x = (individual_a['x'] + individual_b['y'])/2
    new_y = (individual_a['y'] + individual_b['x'])/2

    return {"x": new_x, "y": new_y}

import random



def mutate(individual):
    next_x = individual['x']+random.uniform(-0.1, 0.1)
    next_y = individual['y']+random.uniform(-0.1, 0.1)

    return {"x": next_x, "y": next_y}

def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum(objective_function(individual) for individual in population)

    for i in range(population_size):
        first_choice = select_individual(sorted_by_fitness_population, fitness_sum)
        second_choice = select_individual(sorted_by_fitness_population, fitness_sum)

        individual = crossover(first_choice, second_choice)
        individual = mutate(individual)
        next_generation.append(individual)

    return next_generation

import random

def generate_population(size, x_boundaries, y_boundaries):
    lower_x_boundary, upper_x_boundary = x_boundaries
    lower_y_boundary, upper_y_boundary = y_boundaries

    population = []
    for i in range(size):
        individual = {
            "x": random.uniform(lower_x_boundary, upper_x_boundary),
            "y": random.uniform(lower_y_boundary, upper_y_boundary),
        }
        population.append(individual)

    return population

generations = 100

population = generate_population(size=10, x_boundaries=(-4, 4), y_boundaries=(-4, 4))

i = 1
while True:
    print(f"🧬 GENERATION {i}")

    for individual in population:
        print(individual, objective_function(individual))

    if i == generations:
        break

    i += 1

    population = make_next_generation(population)

best_individual = sort_population_by_fitness(population)[-1]
print("\n🔬 FINAL RESULT")
print(best_individual, objective_function(best_individual))
