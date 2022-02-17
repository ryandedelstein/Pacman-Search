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

from sre_parse import State
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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    #print("Start: ", problem.getStartState())
    #print("Is the start a goal? ", problem.isGoalState(problem.getStartState()))

    # Using the dfs helper 
    path, isPath = dfsHelper(problem, problem.getStartState())
    #path.reverse()
    return path

## DFS Helper, does the work of DFS

def dfsHelper(problem, state):
    curr = state # Current State 
    visited = [] # Visited Nodes 
    fringe = util.Stack() # To be visited fringe 
    visited.append(curr) # Add the start state to visited 
    if problem.isGoalState(curr):
        return [], True
    
    # Get the children of the start and add them to the visited 
    children = problem.expand(curr)
    for i in children:
        if i[0] not in visited:
            fringe.push([i[0], [i[1]]])
    
    # While the fringe is not empty (there are nodes to visit)
    while not fringe.isEmpty():
        curr, path = fringe.pop() # Get the next node 
        visited.append(curr) # Add the current node to visited 
        if problem.isGoalState(curr): # If current is goal, return the path 
            return path, True
        children = problem.expand(curr) # Else, expand the current node 
        for i in children: # Add children to the stack if not visited 
            if i[0] not in visited:
                fringe.push((i[0], path + [i[1]]))
                
    
    return [], False

##recursive dfs without using stack. This is less generalizable 
# def dfsHelper2(problem, state, visited = set()):#
#     curr = state
#     visited.add(curr)
#     if problem.isGoalState(curr):
#         return [], True, visited
#     else:
#         children = problem.expand(curr)
#         nextup = []
#         for i in children:
#             if i[0] not in visited:
#                 nextup.append(i)
#                 visited.add(i[0])
#         for  i in nextup:
#             next = problem.getNextState(curr, i[1])
#             path, ispath, visited = dfsHelper2(problem, next, visited)
#             if ispath:
#                 path.append(i[1])
#                 return path, ispath, visited
#         return [], False, visited

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    path, isPath = bfsHelper(problem, problem.getStartState())
    return path

#BFS helper function to do work of bfs


def bfsHelper(problem, state):
    curr = state # Get the start state
    visited = [] 
    fringe = util.Queue()
    visited.append(curr)
    if problem.isGoalState(curr): 
        return [], True
    
    # Get the children of the start and add to the fringe and visited 
    children = problem.expand(curr)
    for i in children:
        if i[0] not in visited:
            visited.append(i[0])
            fringe.push([i[0], [i[1]]])
    
    # For all nodes in the fringe 
    while not fringe.isEmpty():
        curr, path = fringe.pop() # Get the next node from the q
        if problem.isGoalState(curr): # If goal, return path 
            return path, True
        children = problem.expand(curr) # Expand the current 
        for i in children: 
            if i[0] not in visited: # If child not already visited 
                visited.append(i[0]) # Add to visited 
                fringe.push((i[0], path + [i[1]])) # Push the x,y and cost to of child to fringe 
    
    return [], False

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    path, isPath = aStarHelper(problem, problem.getStartState(), heuristic)
    return path

#Astar helper does work of A* search
def aStarHelper(problem, state, h):
    curr = state # Start state 
    visited = []
    fringe = util.PriorityQueue()
    visited.append(curr) # Add the start to the pq
    if problem.isGoalState(curr):
        return [], True
    
    children = problem.expand(curr) # Get children of start 
    for i in children:
        if i[0] not in visited:
            #visited.append(i[0])
            # Append the children to the fringe 
            # Adding ((x,y), path, cost to get there), heuristic
            fringe.push((i[0], [i[1]], i[2]), i[2] + h(i[0], problem))
    
    # For all nodes in the fringe 
    while not fringe.isEmpty():
        curr, path, cost = fringe.pop() # Current node 
        if curr in visited: # If the node has already been visited, skip 
            continue 
        visited.append(curr) # Else add to the visited 
        if problem.isGoalState(curr): # If goal, return path 
            return path, True
        children = problem.expand(curr) # Get children of the current node 
        for i in children:
            if i[0] not in visited:
                #visited.append(i[0])
                #finge = ((x,y), path to get there , cost to get there)
                fringe.push((i[0], path + [i[1]], cost + i[2]), cost + i[2] + h(i[0],problem))
                
                #fringe.push((i[0], (path + [i[1]], curr[1][1] + i[2])),  curr[1] + i[2] + h(curr, problem))
    return [], False

# Abbreviations
# @Ryan do we need these? or can we comment them? 
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
