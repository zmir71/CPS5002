import random
import string


class Genetic:
    def __init__(self, target, pop_size=100, mutation_rate=0.02):
        self.target = target
        self.pop_size = pop_size
        self.population = self.create_pop()
        self.mutation_rate = mutation_rate
        self.solution = 0

    def create_pop(self):
        letters = string.ascii_lowercase
        population = []
        for i in range(self.pop_size):
            single = ''.join(random.choice(letters) for _ in range(len(self.target)))
            population.append(single)
        return population

    def fitness_score(self, selected):
        return sum(1 for i, j in zip(selected, self.target) if i == j)

    def selection(self):
        fitness_scores = [self.fitness_score(score) for score in self.population]
        total = sum(fitness_scores)
        prob = [f / total for f in fitness_scores]
        return random.choices(self.population,prob,k=self.pop_size)

    def crossover(self, parent1, parent2):
        point = random.randint(1,len(self.target)-1)
        c1 = parent1[:point] + parent2[point:]
        c2 = parent2[:point] + parent1[point:]
        return c1, c2

    def mutation(self, string1):
        letters = string.ascii_lowercase
        return ''.join(char if random.random() > self.mutation_rate else random.choice(letters) for char in string1)

    def replacement(self, offspring):
        self.population = offspring

    def termination(self):
        return any(i == self.target for i in self.population)

    def run(self):
        # Main loop of the genetic algorithm
        while not self.termination():
            self.solution += 1
            selected = self.selection()
            offspring = []
            for i in range(0, len(selected), 2):
                parent1 = selected[i]
                parent2 = selected[i + 1] if i + 1 < len(selected) else selected[i]
                child1, child2 = self.crossover(parent1, parent2)
                offspring.append(self.mutation(child1))
                offspring.append(self.mutation(child2))
            self.replacement(offspring)
            best_individual = max(self.population, key=self.fitness_score)
            print(f"Generation: {self.solution}, Best: {best_individual}, Fitness: {self.fitness_score(best_individual)}")
        print(f"Target string '{self.target}' achieved in {self.solution} generations.")

word = Genetic(target='hello')
word.run()



