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
    """
    Perform DFS with increasingly larger depth.
    Begin with a depth of 1 and increment depth by 1 at every step.
    """
    "*** YOUR CODE HERE ***"
<<<<<<< HEAD
    x = 1;
    while True:
        visited = util.Queue() #hummmmmmm
        solution = util.Queue() #hummmmm
        border = util.Stack() #border??? frontierrr????
=======
    x = 1
    while True:
        visited = util.Queue()
        solution = util.Queue()
        border = util.Stack()
>>>>>>> bee2c6a484ef3e73c121de4e82f92da5fdf280c0
        result = BPLRecursive(problem.getStartState(), problem, x, solution, visited, border)
        x += 1
        if result != 0:            
            return solution.list

def BPLRecursive(node, problem, limit, solution, visited, border):
<<<<<<< HEAD
    # marcar o no visitado???
    # testar se e objetivo
    # se o limite for 0 retorna oque?
    # senaooooooo
        cut = False
        actions = util.Queue()
        for action in problem.getActions(node):
            # aqui vai codigos
        for action in actions.list:
            # aqui vai codigos
=======
    visited.push(node)
    if problem.goalTest(node):
        return True
    elif limit == 0:
        return 0
    else:
        cut = False
        actions = util.Queue()
        for action in problem.getActions(node):
            child = problem.getResult(node, action)
            border.push(child)
            actions.push(action)
        for action in actions.list:
            child = border.pop()
            if visited.list.count(child) == 0 and border.list.count(child) == 0:
                result = BPLRecursive(child, problem, limit - 1, solution, visited, border)
                if result == 0:
                    cut = True
                elif result is not None:
                    print(action)
                    solution.push(action)
                    return True
>>>>>>> bee2c6a484ef3e73c121de4e82f92da5fdf280c0
        if cut:
            return 0
        else:
            return None
<<<<<<< HEAD
=======


# manhattanHeuristic: Heuristica que calcula a quantos saltos faltam para chegar no objetivo
#                     desconsiderando as paredes

# euclideanHeuristic: Calcula a distancia em linha reta ate o objetivo
>>>>>>> bee2c6a484ef3e73c121de4e82f92da5fdf280c0

def aStarSearch(problem, heuristic=nullHeuristic):
    # print(dir(problem))
    # print problem.getResult((1,1),'West')
    # exit(-10)
    visited = []
    border = util.PriorityQueue()
    start = problem.getStartState()
    border.push( (start, []), 0)

    while not border.isEmpty():
        node, actions = border.pop()

        if problem.goalTest(node):
            return actions

        visited.append(node)

        for action in problem.getActions(node):
            next = problem.getResult(node, action)
            if not next in visited:
                new_actions = actions + [action]
                score = problem.getCostOfActions(new_actions) + heuristic(next, problem)
                border.push( (next, new_actions), score)
    return []

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch