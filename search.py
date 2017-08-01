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
    return [s, s, w, s, w, w, s, w]


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

cutoff = 'cutoff'

def iterativeDeepeningSearch(problem):
    """
    Perform DFS with increasingly larger depth.
    Begin with a depth of 1 and increment depth by 1 at every step.
    python pacman.py -l tinyMaze -p SearchAgent -a fn=ids
    goal: objetivo, meta
    walls: paredes
    """
    "*** YOUR CODE HERE ***"
    print(dir(problem))
    # util.raiseNotDefined()
    print("Posicao inicial:" + str(problem.getStartState()))
    print("Paredes:")
    print(problem.walls)
    listaParedes = problem.walls.asList()
    ultimo = listaParedes[-1]
    print 'Total de campos: ',  ((ultimo[0]) + 1) * ((ultimo[1]) + 1)
    print 'Total sem as paredes externas: ',  ((ultimo[0]) - 1) * ((ultimo[1]) - 1)


    # function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
    # for depth = 0 to inf do
    # result <- DEPTH-LIMITED-SEARCH(problem,depth)
    # if result != cutoff then return result

    visitedNodes = []
    caminho = []
    caminho.append(problem.getStartState())
    acoes = []
    while(True):
        # print(caminho)

        # raw_input()
        try:
            no = caminho.pop()
        except Exception:
            pass
        visitedNodes.append(no)
        if(problem.goalTest(no)):
            print 'no final'
            break
        else:
            for action in problem.getActions(no):
                if(action =='North'):
                    filho = (no[0], no[1] + 1)
                if(action =='South'):
                    filho = (no[0], no[1] -1)
                if(action =='East'):
                    filho = (no[0]+1, no[1])
                if(action =='West'):
                    filho = (no[0] - 1, no[1])
                
                if(filho not in visitedNodes):
                    caminho.append(filho)
                else:
                    continue
            

    # # while(depth < 2):
    #     result = depthLimitedSearch(problem, depth)
    #     # raw_input('')
    #     print '=========================='
    #     depth = depth + 1
    #     if(result != cutoff):
    #         print 'deu'
    #         print result
    #         break


    # # Montar uma lista com o tamanho total de campos
    # listaTotal = []
    # for x in range(ultimo[0] + 1):
    #     for y in range(ultimo[1] + 1):
    #         s = (x, y)
    #         if(s not in listaParedes):
    #             listaTotal.append(s)
    # # Pegar a diferenca entre a lista total e a de paredes
    # print(listaTotal)
    # grafo = []
    # for p in listaTotal:
    #     try:
    #         print(p)
    #         movimentos = problem.getActions(p)
    #         if(len(movimentos) != 0):
    #             no = {
    #                 'posicao': p,
    #                 'movimentos': movimentos,
    #                 'visitado': False
    #             }
    #             print no
    #             grafo.append(no)
    #     except IndexError:
    #         print('IndexError')
    #         continue
    # # print(len(grafo))
    # print("Movimentos possiveis:")
    # for no in grafo:
    #     print(no)

    # for data in problem.walls.data:
    #     print(data)

    # print("Objetivo:" + str(problem.goal))

    # # print(problem.getActions((3,2)))
    # # print(problem.getCostOfActions(problem.getActions((1,1))))
    # problem.visualize
    # from time import sleep
    # try:
    #     sleep(100)
    # except KeyboardInterrupt:
    #     print('continuar')
    # acoes = ['South', 'South', 'West', 'South','West', 'West', 'South', 'West', ]
    # acoes = ['West','West','West','West','South','South','East','South','South','West',]
    return acoes
    """
    O retorno da funcao deve ser uma lista contendo as acoes necessarias, 
    em sequencia, para que o Pacman consiga pegar a comida. 
    """
    # util.raiseNotDefined()


# function DEPTH-LIMITED-SEARCH(problem,limit) returns a solution, or failure/cutoff
# return RECURSIVE-DLS(MAKE-NODE(problem.INTIAL-STATE),problem,limit)

# visitedNodes = []

# def depthLimitedSearch(problem, limit):
#     visitedNodes.append(problem.getStartState())

#     if(problem.goalTest(no)):

#     return recursiveDLS(problem.getStartState(), problem, limit)

# def recursiveDLS(no, problem, limit):
#     # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
#     if(problem.goalTest(no)):
#         print no
#         print 'No final encontrado'
#         return no
#     # else if limit = 0 then return cutoff
#     elif (limit == 0):
#         return cutoff
#     # else
#     else:
#         # cutoff_occurred? <- false
#         cutoff_occurred = False
#         for action in problem.getActions(no):
#             # child <- CHILD-NODE(problem,node,action)  
#             if(action =='North'):
#                 filho = (no[0], no[1] + 1)
#             if(action =='South'):
#                 filho = (no[0], no[1] -1)
#             if(action =='East'):
#                 filho = (no[0]+1, no[1])
#             if(action =='West'):
#                 filho = (no[0] - 1, no[1]) 
#             # result <- RECURSIVE-DLS(child,problem,limit-1)
#             result = recursiveDLS(filho, problem, limit-1)
#             # if result = cutoff then cutoff_occurred? <- true
#             if(result == cutoff):
#                 cutoff_occurred = True
#             # else if result != failure then return result
#             elif(result != False):
#                 return result
#         # if cutoff_occurred? then return cutoff else return failure
#         if(cutoff_occurred):
#             return cutoff
#         else:
#             return False

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch
