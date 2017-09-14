# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
from searchAgents import mazeDistance
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)

        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # score do estado atual
        score = successorGameState.getScore()

        # Para o estado de cada fantasma, calcular heuristica de manhattan a partir
        # de estado de pacman, caso distancia minima (2) & fantasma nao assustado,
        # retorna pontuacao negativa
        for ghost in newGhostStates:
            dist = manhattanDistance(newPos, ghost.getPosition())
            if dist < 2 and ghost.scaredTimer == 0:
                return -99
        foodScore = 0

        # Para cada comida, calcular heuristica manhattan
        # filtra o valor da comida com menor dist
        # retorna valor adicionando score atual
        for food in newFood.asList():
            dist = manhattanDistance(newPos, food)
            if dist < foodScore or foodScore is 0:
                foodScore = dist
        if foodScore > 0:
            foodScore = 1.0 / foodScore
        return foodScore + score


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent & AlphaBetaPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 7)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        result = self.max(gameState, self.depth)
        return result

    def min(self, gameState, depth, agent = 1):
        result = []
        if gameState.isLose() or gameState.isWin() or depth is 0:
            return self.evaluationFunction(gameState)

        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if agent < gameState.getNumAgents() - 1:
                result.append(self.min(successor, depth, agent + 1))
            else:
                result.append(self.max(successor, depth - 1))

        return min(result)

    def max(self, gameState, depth):
        result = {}
        scores = []
        if gameState.isLose() or gameState.isWin() or depth is 0:
            return self.evaluationFunction(gameState)
        if depth > 0:
            for action in gameState.getLegalActions(0):
                minVal  = self.min(gameState.generateSuccessor(0, action), depth)
                scores.append(minVal)
                result[minVal] = action

        if depth is self.depth:
            return result[max(scores)]
        elif list:
            return max(scores)



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 8)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        result = self.max(gameState, self.depth)
        return result

    def expect(self, gameState, depth, agent = 1):
        if gameState.isLose() or gameState.isWin() or depth is 0:
            return self.evaluationFunction(gameState)
        sum = 0
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if agent < gameState.getNumAgents() - 1:
                sum += self.expect(successor, depth, agent + 1)
            else:
                sum += self.max(successor, depth - 1)

        return sum / len(gameState.getLegalActions(agent))

    def max(self, gameState, depth):
        result = {}
        scores = []
        if gameState.isLose() or gameState.isWin() or depth is 0:
            return self.evaluationFunction(gameState)
        if depth > 0:
            for action in gameState.getLegalActions(0):
                expectVal  = self.expect(gameState.generateSuccessor(0, action), depth)
                scores.append(expectVal)
                result[expectVal] = action

        if depth is self.depth:
            return result[max(scores)]
        elif list:
            return max(scores)



def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 9).

      DESCRIPTION: <write something here so we know what you did>

    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    score = currentGameState.getScore()

    for ghost in newGhostStates:
        dist = manhattanDistance(newPos, ghost.getPosition())
        if dist < 6.0 and ghost.scaredTimer == 0 and not flag:
            flag = not flag
            return -99
    foodScore = 0
    for food in newFood.asList():
        dist = manhattanDistance(newPos, food)
        if dist < foodScore or foodScore is 0:
            foodScore = dist
    if foodScore > 0:
        foodScore = 1.0 / foodScore

    capsuleScore = 0
    for capsule in currentGameState.getCapsules():
        dist = manhattanDistance(newPos, capsule)
        if dist > capsuleScore or capsuleScore is 0:
            capsuleScore = dist
    if capsuleScore > 0:
        capsuleScore = 1.0 / capsuleScore
    return (foodScore - capsuleScore) + score
    """
    sum = 0
    legalMoves = currentGameState.getLegalActions()
    for action in legalMoves:
        sum += func(currentGameState, action)
    if legalMoves:
        return (sum/len(legalMoves)) + currentGameState.getScore() - random.random()
    else:
        return currentGameState.getScore()

def func(currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)

    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    if(successorGameState.isWin() or newPos in successorGameState.getCapsules()):
        return -10000000

    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    score = successorGameState.getScore()

    for ghost in newGhostStates:
        dist = manhattanDistance(newPos, ghost.getPosition())
        if dist < 2 and ghost.scaredTimer == 0:
            return -99
    foodScore = 0
    for food in newFood.asList():
        dist = manhattanDistance(newPos, food)
        if dist < foodScore or foodScore is 0:
            foodScore = dist
    if foodScore > 0:
        foodScore = 1.0 / foodScore
    return foodScore + score

# Abbreviation
better = betterEvaluationFunction

