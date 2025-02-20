# Name: [Your chosen name for the metaheuristic]
# Code:
import sys
from pathlib import Path
import numpy as np
project_dir = Path(__file__).resolve().parents[2] # Remember to write well this line: 'project_dir = Path(__file__).resolve().parents[2]'
sys.path.insert(0, str(project_dir))
import benchmark_func as bf
import metaheuristic as mh

fun = bf.{self.benchmark_function}({self.dimensions}) # This is the selected problem
prob = fun.get_formatted_problem()

heur = [
    (  # Search operator 1
        '[operator_name]',
        {
            'parameter1': value1,
            'parameter2': value2,
            more parameters as needed
        },
        '[selector_name]'
    ),
    (
        '[operator_name]',
        {
            'parameter1': value1,
            'parameter2': value2,
            ... more parameters as needed
        },
        '[selector_name]'
    )
]

met = mh.Metaheuristic(prob, heur, num_iterations=100)
#met.verbose = True # please comment this line
#met.run() # please comment this line

#print('x_best = {}, f_best = {}'.format(*met.get_solution()))

# Initialise the fitness register
fitness = []
# Run the metaheuristic with the same problem 30 times
for rep in range(30):
    met = mh.Metaheuristic(prob, heur, num_iterations=1000, num_agents={self.num_of_agents})  
    met.reset_historicals()
    met.verbose = False
    met.run()
    #print('rep = {}, x_best = {}, f_best = {}'.format(rep+1, *met.get_solution()))
    
    fitness.append(met.historical['fitness'])

fitness_array = np.array(fitness).T
final_fitness = np.array([x[-1] for x in fitness_array.T])
print("final_fitness_array", final_fitness)

# Short explanation and justification:
# [Your explanation here, each line starting with '#']
