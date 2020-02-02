# Imports 
import random 
import heapq
from math import sqrt
# Variable Declarations
map_maze = {
    'A': {
        'adjacent': [('B', 5)], 
        'point': (1, 1)
    },
    'B': {
        'adjacent': [('A', 5), ('C', 7), ('F', 2)], 
        'point': (1, 6)
    },
    'C': {
        'adjacent': [('B', 7), ('L', 8)], 
        'point': (1, 13)
    },
    'D': {
        'adjacent': [('E', 3)], 
        'point': (3, 1)
    },
    'E': {
        'adjacent': [('D', 3), ('I', 6)],
        'point': (3, 4)
    },
    'F': {
        'adjacent': [('B', 2), ('G', 5), ('J', 6)], 
        'point': (3, 6)
    },
    'G': {
        'adjacent': [('F', 5), ('K', 6)],
        'point': (3, 11)
    },
    'H': {
        'adjacent': [('I', 3)],
        'point': (9, 1)
    },
    'I': {
        'adjacent': [('E', 6), ('J', 2)],
        'point': (9, 4)
    },
    'J': {
        'adjacent': [('F', 6), ('I', 2), ('K', 5), ('O', 2)],
        'point': (9, 6)
    },
    'K': {
        'adjacent': [('G', 6), ('J', 5), ('L', 2), ('T', 9)],
        'point': (9, 11)
    },
    'L': {
        'adjacent': [('C', 8), ('K', 2), ('U', 9)],
        'point': (9, 13)
    },
    'M': {
        'adjacent': [('N', 3)],
        'point': (11, 1)
    },
    'N': {
        'adjacent': [('M', 3), ('O', 2), ('R', 7)],
        'point': (11, 4)
    },
    'O': {
        'adjacent': [('J', 2), ('N', 2), ('P', 3)],
        'point': (11, 6)
    },
    'P': {
        'adjacent': [('O', 3), ('S', 7)],
        'point': (11, 9)
    },
    'Q': {
        'adjacent': [('R', 3)],
        'point': (18, 1)
    },
    'R': {
        'adjacent': [('N', 7), ('Q', 3), ('S', 5)],
        'point': (18, 4)
    },
    'S': {
        'adjacent': [('P', 7), ('R', 5), ('T', 2)],
        'point': (18, 9)
    },
    'T': {
        'adjacent': [('K', 9), ('S', 2), ('U', 2)],
        'point': (18, 11)
    },
    'U': {
        'adjacent': [('L', 9), ('T', 2)],
        'point': (18, 13)
    }
}

first_state = 'A'
objective_state = 'Q'

result = [(first_state, 0)]
visited = []
#fronteira que armazenara os estados descobertos em fila de prioridade de acordo com o custo
frontier = []
heuristics = {}
heapq.heappush(frontier, (0, first_state, first_state))

#pré calcula as heuristicas de cada ponto até o ponto do objetivo
def calc_heuristics():
    global map_maze

    xGoal, yGoal = map_maze[objective_state]['point']

    for k in map_maze.keys():
        xState, yState = map_maze[k]['point']
        heuristics.update({k : sqrt((xState - xGoal)**2) + ((yState - yGoal)**2)})

def get_adjacent(state):
  return map_maze[state]['adjacent']

calc_heuristics()
print(heuristics)

while len(frontier) != 0:

  print(frontier)
  cost, state_, path = heapq.heappop(frontier)
  # print(cost, state_)
  if (state_ not in visited):
    visited.append(state_)

    if state_ == objective_state:
      print('\nCaminho resultante: %s' %path)
      print('Custo: %s' %cost)
      break
    
    for child in get_adjacent(state_):
      if (child[0] not in visited):
        count_cost = cost + child[1] + heuristics[child[0]]
        result.append((state_ + '->' + child[0], count_cost))
        #adiciona a fronteira o custo, o nome do estado adjacente e o caminho para chegar até ele
        heapq.heappush(frontier, (count_cost, child[0], path + '->' + child[0]))

#print(get_adjacent(first_state))