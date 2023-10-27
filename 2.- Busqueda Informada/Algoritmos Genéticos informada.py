

import random

# Función de aptitud (fitness) que define el problema a resolver.
def fitness(individual):
    target = "Hello, World!"
    score = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            score += 1
    return score

# Función para crear una población inicial de individuos aleatorios.
def create_population(pop_size, gene_length):
    population = []
    for _ in range(pop_size):
        individual = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!?") for _ in range(gene_length))
        population.append(individual)
    return population

# Función para seleccionar a los individuos más aptos.
def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        parents.append(max(population, key=fitness))
        population.remove(parents[-1])
    return parents

# Función para realizar el cruce (crossover) entre dos padres y crear un hijo.
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Función para aplicar una mutación a un individuo con una probabilidad dada.
def mutate(individual, mutation_rate):
    mutated_individual = ""
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,.!?")
        else:
            mutated_individual += gene
    return mutated_individual

# Parámetros del algoritmo
population_size = 100
gene_length = len("Hello, World!")
num_generations = 100
num_parents = 20
mutation_rate = 0.01

# Generar la población inicial
population = create_population(population_size, gene_length)

# Evolución del algoritmo
for generation in range(num_generations):
    parents = select_parents(population, num_parents)
    next_generation = parents.copy()

    while len(next_generation) < population_size:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        next_generation.append(child)

    population = next_generation

    best_individual = max(population, key=fitness)
    print(f"Generación {generation}: {best_individual} (Fitness: {fitness(best_individual)})")

# Resultado final
best_individual = max(population, key=fitness)
print("Mejor individuo encontrado:", best_individual)
print("Fitness:", fitness(best_individual))