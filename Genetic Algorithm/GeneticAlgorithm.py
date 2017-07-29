'''A sample genetic algorithm implementation using python'''
import random
import math
import functools

#setup parameter

mutation_rate = 0.01
options = ''.join(chr(i) for i in range(65, 97+26)) + ' '

class DNA:

  def __init__(self, target, random):
    self.target = target
    self.random = random

  @property
  def fitness(self):
    #you can use this imperative style
    
    # score = 0
    # for t, r in zip(self.target, self.random):
    #   if t == r:
    #     score += 1
    # return (score/len(self.target)) * 100

    #functional implementation
    score = functools.reduce(lambda score, atuple:
                              score + 1 if atuple[0] == atuple[1] else score,
                              zip(self.target, self.random),
                              0)
    return (score / len(self.target)) * 100
  
  def crossover(self, mate):
    #lets choose the random between 0 and length of target
    r = random.choice(range(len(self.target) - 1 ))
    return DNA(self.target, self.random[: r] + 
                            mate.random[r: ])

  def mutate(self):
    self.random = ''.join(random.choice(options) if random.random() < mutation_rate else i 
                                                                      for i in self.random)
  def __repr__(self):
    return 'Random: {}, Fitness: {}'.format(self.random, self.fitness)
  
  def target_matched(self):
    return self.random == self.target

class Genetic:
  
  def __init__(self, n, target):
    self.n = n #number of population
    #initial population 
    self.population = [DNA(target, ''.join(random.choice(options) 
                      for i in range(len(target)))) for i in range(n)] 
    self.mutation_stop = False
    self.total_generation = 0
  
  def generate_mating_pool(self):
    self.pool = []
    #maximum fitness
    max_dna = max(self.population, key=lambda dna: dna.fitness)
    print(max_dna)
    max_fitness = max_dna.fitness
    #append each DNA object according to their fitness score
    for dna in self.population:
      t = math.floor(dna.fitness / max_fitness * 100)
      for i in range(t):
        self.pool.append(dna)
  
  def reproduce(self):
    #pick two parents
    self.population = []
    for i in range(self.n):
      parent_a = random.choice(self.pool)
      parent_b = random.choice(self.pool)

      child = parent_a.crossover(parent_b)
      child.mutate()
      self.population.append(child)
    self.total_generation += 1
  
  def evaluate(self):
    # if any(dna.target_matched() for dna in self.population):
    #   self.mutation_stop = True
    for dna in self.population:
      if dna.target_matched():
        print('Found ', dna.random)
        self.mutation_stop = True
        break

def main():
  n = 1500 #number of initial population for 
  target = 'To be or not to be'
  _genetic = Genetic(n, target)

  while True:
    if _genetic.mutation_stop:
      break
    _genetic.generate_mating_pool()
    _genetic.reproduce()
    _genetic.evaluate()
  print('Total Population: ', _genetic.n)
  print('Mutation Rate: ', mutation_rate)
  print('Total generation: ', _genetic.total_generation)
  

if __name__ == '__main__':
  main()
