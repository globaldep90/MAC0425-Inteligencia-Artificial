# Yara Grassi Gouffon
# NUSP 4172560

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

        from util import manhattanDistance
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        res = 0

        # Check ghosts
        for ghostState in newGhostStates:
          dist = manhattanDistance(ghostState.getPosition(), newPos)
          if dist <= 2: # Flee from the ghosts!
            res += -400 + 50*dist

        # Will I eat food?
        if successorGameState.getNumFood() < currentGameState.getNumFood():
          res += 100
        else: #Head toward nearest food
          foodlist = newFood.asList()
          if len(foodlist)>0:
            foodDist = min([manhattanDistance(food, newPos) for food in foodlist])
            res += 100 - foodDist

        # Is there a capsule?
        if newPos in currentGameState.getCapsules():
          res += 140

        # Avoid dead ends
        walls = successorGameState.getWalls()
        wallCount = sum([walls[newPos[0]+1][newPos[1]], walls[newPos[0]-1][newPos[1]], walls[newPos[0]][newPos[1]+1], walls[newPos[0]][newPos[1]-1]])
        if wallCount >= 3:
          res -= 350

        return res

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
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

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
      Your minimax agent (question 2)
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
        "*** YOUR CODE HERE ***"

        def maxValue(gameState, curDepth):
          curDepth += 1
          if curDepth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          value = float('-inf')
          actions = gameState.getLegalActions(0)
          for action in actions:
            value = max(value, minValue(gameState.generateSuccessor(0, action), curDepth, 1))
          return value

        def minValue(gameState, curDepth, agent):
          if curDepth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          value = float('inf')
          actions = gameState.getLegalActions(agent)

          if agent < gameState.getNumAgents()-1:
            for action in actions:
              value = min(value, minValue(gameState.generateSuccessor(agent, action), curDepth, agent+1))
          else:
            for action in actions:
              value = min(value, maxValue(gameState.generateSuccessor(agent, action), curDepth))
          return value

        bestAction = None
        bestValue = float('-inf')
        actions = gameState.getLegalActions(0)
        for action in actions:
          value = minValue(gameState.generateSuccessor(0, action), 0, 1)
          if(value>bestValue):
            bestValue = value
            bestAction = action
        return bestAction

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def maxValue(gameState, alpha, beta, curDepth):
          curDepth += 1
          if curDepth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          value = float('-inf')
          actions = gameState.getLegalActions(0)
          for action in actions:
            value = max(value, minValue(gameState.generateSuccessor(0, action), alpha, beta, curDepth, 1))
            if value > beta:
              return value
            alpha = max(alpha, value)
          return value

        def minValue(gameState, alpha, beta, curDepth, agent):
          if curDepth == self.depth or gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState)

          value = float('inf')
          actions = gameState.getLegalActions(agent)

          if agent < gameState.getNumAgents()-1:
            for action in actions:
              value = min(value, minValue(gameState.generateSuccessor(agent, action),alpha, beta, curDepth, agent+1))
              if value < alpha:
                return value
              beta = min(beta, value)
          else:
            for action in actions:
              value = min(value, maxValue(gameState.generateSuccessor(agent, action), alpha, beta, curDepth))
              if value < alpha:
                return value
              beta = min(beta, value)
          return value

        bestAction = None
        bestValue = float('-inf')
        actions = gameState.getLegalActions(0)
        alpha = float('-inf')
        for action in actions:
          value = minValue(gameState.generateSuccessor(0, action), alpha, float('inf'), 0, 1)
          alpha = max(alpha, value)

          if(value>bestValue):
            bestValue = value
            bestAction = action
        return bestAction