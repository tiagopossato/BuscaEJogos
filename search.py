# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import sys
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def goalTest(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
        Given a state, returns available actions.
        Returns a list of actions
        """        
        util.raiseNotDefined()

    def getResult(self, state, action):
        """
        Given a state and an action, returns resulting state.
        """
        util.raiseNotDefined()

    def getCost(self, state, action):
        """
        Given a state and an action, returns step cost, which is the incremental cost 
        of moving to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    You are not required to implement this, but you may find it useful for Q5.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def iterativeDeepeningSearch(problem):
    print(dir(problem))
    # util.raiseNotDefined()
    print("Posicao inicial:" + str(problem.getStartState()))
    print("Paredes:")
    print(problem.walls)
    listaParedes = problem.walls.asList()
    ultimo = listaParedes[-1]
    print 'Total de campos: ',  ((ultimo[0])+1) * ((ultimo[1])+1)
    print 'Total sem as paredes externas: ',  ((ultimo[0])-1) * ((ultimo[1])-1)

    # Montar uma lista com o tamanho total de campos
    listaTotal = []
    grafo = []

    for x in range(ultimo[0]+1):
        for y in range(ultimo[1]+1):
            s = (x,y)
            if(s not in listaParedes):
                listaTotal.append(s)
                movimentos = problem.getActions(s)
                if(len(movimentos)!=0):
                    no = {
                        'posicao' : s,
                        'movimentos' : movimentos
                    }
                    grafo.append(no)
    # Pegar a diferenca entre a lista total e a de paredes
    print(listaTotal)

    # print(len(grafo))
    print("Movimentos possiveis:")
    for no in grafo:
        print(no)
    
    # for data in problem.walls.data:
        # print(data)

    # print("Objetivo:" + str(problem.goal))

    # print(problem.getActions((3,2)))
    # print(problem.getCostOfActions(problem.getActions((1,1))))
    """print(problem.getStartState())

    problem.visualize
    from time import sleep
    try:
        sleep(1)
    except KeyboardInterrupt:
        print('continuar')
    """
    # acoes = ['South', 'South', 'West', 'South', 'West', 'West', 'South', 'West',]
    # acoes = ['West','West','West','West','South','South','East','South','South','West',]
    acoes = ['']
    # print problem.actions(problem.getActions((1,1)))
    estado_atual2 = problem.getStartState()
    estado_back = problem.getStartState()

    # estado_back.append(estado_atual2)
    # print(estado_back)
    
    for x in xrange(0, 100):
        # arrumar esse if, aqui ta o problema
        if (estado_atual2 not in estado_back): 
            print("entrou")
            if (problem.getActions(estado_atual2)[1] == 'North'):
                # estado_back.append(estado_atual2)
                # print("ESTADO BACK: ", estado_back)
                estado_atual2 = (estado_atual2[0],estado_atual2[1]+1) 
                acoes.append('North') 
                print(estado_atual2) 
            elif (problem.getActions(estado_atual2)[1] == 'South'):
                # estado_back.append(estado_atual2)
                # print("ESTADO BACK: ", estado_back)
                estado_atual2 = (estado_atual2[0],estado_atual2[1]-1)
                acoes.append('South')
                print(estado_atual2) 
            elif (problem.getActions(estado_atual2)[1] == 'West'):
                # estado_back.append(estado_atual2)
                # print("ESTADO BACK: ", estado_back)
                estado_atual2 = (estado_atual2[0]-1,estado_atual2[1])
                acoes.append('West')
                print(estado_atual2) 
            elif (problem.getActions(estado_atual2)[1] == 'East'):
                # estado_back.append(estado_atual2)
                # print("ESTADO BACK: ", estado_back)
                estado_atual2 = (estado_atual2[0]+1,estado_atual2[1])
                acoes.append('East')
                print(estado_atual2)
    
    acoes.pop(0)
    
    print(acoes)
    # print problem.goalTest()
    return acoes    

    """
    Perform DFS with increasingly larger depth.

    Begin with a depth of 1 and increment depth by 1 at every step.
    """
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
