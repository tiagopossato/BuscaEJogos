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
from compiler import visitor

import util
import sys
import copy
import time

from collections import namedtuple


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
    node = problem.getStartState()

    border = util.Queue()
    border.push(node)
    visited = util.Queue()
    paths = {}
    paths[node] = []
    while not border.isEmpty():
        node = border.pop()
        visited.push(node)
        if problem.goalTest(node):
            return paths[node]
        for action in problem.getActions(node):
            child = problem.getResult(node, action)
            if child not in visited.list and child not in border.list:
                border.push(child)
                paths[child] = paths[node] + [action]


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
    x = 1
    while True:
        visited = util.Queue()
        solution = util.Queue()
        border = util.Stack()
        result = BPLRecursive(problem.getStartState(), problem, x, solution, visited, border)
        x += 1
        if result != 0:
            return solution.list

def BPLRecursive(node, problem, limit, solution, visited, border):
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
                    solution.push(action)
                    return True
        if cut:
            return 0
        else:
            return None


# manhattanHeuristic: Heuristica que calcula a quantos saltos faltam para chegar no objetivo
#                     desconsiderando as paredes

# euclideanHeuristic: Calcula a distancia em linha reta ate o objetivo

#Funcao aStarSearch, funcao que serve para encontrar o melhor caminho para o objetivo 
#levando em conta a heuristica que e o custo de cada acao.
def aStarSearch(problem, heuristic=nullHeuristic):
    #Pegando o estado inicial na variavel start
    start = problem.getStartState()
    #criando uma fila de prioridade para a borda
    border = util.PriorityQueue()
    #calculando a heuristica com o ponto do inicio e o problema
    actual_state_cost = heuristic(start,problem)
    visited = []
    visited_nodes = util.Queue()
    #adicionando o primeiro no visitado como o no de inicio
    visited_nodes.push(start)
    #chamada recursiva para ir salvando os nos visitados e saber qual o melhor caminho
    #aqui ira ser passado o custo atual, a heuristica e os nos visitados.
    visited = recursive_astar_search(problem, start, border, actual_state_cost, heuristic, visited, visited_nodes)

    return visited

def recursive_astar_search(problem, start, border, actual_state_cost, heuristic, visited, visited_nodes):
    #While true para ele ficar fazendo sempre enquanto nao encontrar o final.
    while True:
    #teste para saber se chegou ao final
        if problem.goalTest(start):
        #se chegar ao fim, sai da funcao recursiva com o return dos nos visitados
            return visited
      #caso nao tenha terminado, uma lista de acoes recebe as acoes possiveis do no inicial.
        actions = problem.getActions(start)


        for action in actions:
        #salva os nos visitados nessa variavel new_visited
            new_visited = copy.copy(visited)
            new_visited.append(action)
            #resulting_state recebe o retorno do resultado da acao start do no atual 
            resulting_state = problem.getResult(start, action)
            #custo da acao, com a funcao getCost pode-se calcular qual sera o menor custo, assim que o aStar sabe quando ele deve
            #seguir pelo caminho que esta ou mudar de direcao.
            action_cost = problem.getCost(start,action)
            #nesta variavel e calculado o custo atual de chegada menos a heuristica atual
            cost_so_far = actual_state_cost - heuristic(start, problem) 

            #se existir um custo do estado sem a heuristica, deve ser contabilizado, se nao, contar somente a heuristica + o custo ate o fim.
            if action_cost:
                action_cost = heuristic(resulting_state, problem) + action_cost + cost_so_far
            else:
                action_cost = heuristic(resulting_state, problem) + cost_so_far

            #a lista de borda recebe o no e o custo dele.
            border.push((resulting_state, action_cost, new_visited), action_cost)

        new_node_found = False 
 
        while not new_node_found:
            #se a borda estiver vazia, quer dizer que nao tem nada, entao retorna false com problema de nao chegar no fim. 
            if border.isEmpty():
                return False

            #aqui e salvo o no que acaba de ser desempilhado da borde
            (start, actual_state_cost, visited) = border.pop()

            #se o no start ou seja, o no atual, nao estiver na lista dos visitados entao a lista de visitados adiciona o no atual, caso contrario nao.
            if start not in visited_nodes.list:
                visited_nodes.push(start)
                new_node_found = True

# Abbreviations
bfs = breadthFirstSearch
astar = aStarSearch
ids = iterativeDeepeningSearch