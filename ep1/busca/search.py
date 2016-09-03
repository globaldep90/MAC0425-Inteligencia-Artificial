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

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
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

def returnSolution(start, goal):
    parent = goal
    solution = []
    while parent[0]!=start:
        solution.append(parent[2])
        parent = parent[1]
    # print "Solution:", solution[::-1]
    return solution[::-1]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack
    frontier = Stack()
    generated  = {}
    frontier.push((problem.getStartState(), None, None))
    while not frontier.isEmpty():
        currentNode = frontier.pop()
        if problem.isGoalState(currentNode[0]):
            return returnSolution(problem.getStartState(), currentNode)
        if generated.has_key(currentNode[0]):
            continue
        generated[currentNode[0]] = 1 #Explored
        successors = problem.getSuccessors(currentNode[0])
        for successor in successors:
            node = (successor[0], currentNode, successor[1])
            frontier.push(node)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    frontier = Queue()
    generated  = {}
    frontier.push((problem.getStartState(), None, None))
    while not frontier.isEmpty():
        currentNode = frontier.pop()
        if problem.isGoalState(currentNode[0]):
            return returnSolution(problem.getStartState(), currentNode)
        generated[currentNode[0]] = 1 #Explored
        successors = problem.getSuccessors(currentNode[0])
        for successor in successors:
            node = (successor[0], currentNode, successor[1])
            if not generated.has_key(successor[0]):
                frontier.push(node)
                generated[successor[0]] = 2 #In frontier

def iterativeDeepeningSearch(problem):
    """
    Start with depth = 0.
    Search the deepest nodes in the search tree first up to a given depth.
    If solution not found, increment depth limit and start over.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    "*** YOUR CODE HERE ***"
    limit = 0
    while True:
        solution = depthLimitedSearch(problem, limit)
        if solution != -1:
            return solution
        limit += 1

def depthLimitedSearch(problem, limit):
    from util import Stack
    frontier = Stack()
    generated  = {}
    frontier.push((problem.getStartState(), None, None, 0, 0))
    while not frontier.isEmpty():
        currentNode = frontier.pop()
        if problem.isGoalState(currentNode[0]):
            return returnSolution(problem.getStartState(), currentNode)
        if currentNode[4] == limit:
            continue
        if generated.has_key(currentNode[0]):
            if currentNode[3] > generated[currentNode[0]]:
                continue
        generated[currentNode[0]] = currentNode[3] #Explored & mark cost
        successors = problem.getSuccessors(currentNode[0])
        for successor in successors:
            node = (successor[0], currentNode, successor[1], currentNode[3]+successor[2], currentNode[4]+1)
            frontier.push(node)
    return -1

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    frontier = PriorityQueue()
    generated  = {}
    frontier.push((problem.getStartState(), None, None, 0), 0)
    while not frontier.isEmpty():
        currentNode = frontier.pop()
        if problem.isGoalState(currentNode[0]):
            return returnSolution(problem.getStartState(), currentNode)
        generated[currentNode[0]] = -1 #Explored
        successors = problem.getSuccessors(currentNode[0])
        for successor in successors:
            node = (successor[0], currentNode, successor[1], currentNode[3]+successor[2])
            if not generated.has_key(successor[0]):
                frontier.push(node, node[3])
                generated[successor[0]] = node[3] #In frontier
            elif generated[successor[0]] > node[3]:
                frontier.push(node, node[3])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    frontier = PriorityQueue()
    generated  = {}
    frontier.push((problem.getStartState(), None, None, 0), 0)
    while not frontier.isEmpty():
        currentNode = frontier.pop()
        if problem.isGoalState(currentNode[0]):
            return returnSolution(problem.getStartState(), currentNode)
        generated[currentNode[0]] = -1 #Explored
        successors = problem.getSuccessors(currentNode[0])
        for successor in successors:
            node = (successor[0], currentNode, successor[1], currentNode[3]+successor[2])
            if not generated.has_key(successor[0]):
                frontier.push(node, node[3]+heuristic(node[0], problem))
                generated[successor[0]] = node[3] #In frontier
            elif generated[successor[0]] > node[3]:
                frontier.push(node, node[3]+heuristic(node[0], problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch