# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:55:16 2017

@author: Weigo
"""

import numpy as np
import matplotlib.pyplot as plt

DNA_SIZE = 8  
POP_SIZE = 100
CROSS_RATE = 0.8
MUTATION_RATE = 0.02
N_GENERATIONS = 250
X_BOUND = [0,5]

# 0000 0000
# 0011 1100
# 0000 0"1"00 -> child mutation  
def F(x): return np.sin(10 * x) * x + np.cos(2 * x) * x

def get_fitness(pred): return pred

def slateDNA(pop):
    pass

def translateDNA(pop):
    pass

def select(pop, fitness):
    pass

def crossover(parent, pop):
    pass

def mutate(child):
    pass

for _ in range()