import sys
import time

winningState = "012345678"


def main():
    search_type = sys.argv[1]
    initial_state = sys.argv[2].translate(str.maketrans({",": ""}))

    print(dfs_solution(initial_state))
    # print(find_neighbors(initial_state))


def dfs_solution(initial_state):
    frontier = StackFrontier()
    explored = set()
    parents = {}

    frontier.push(initial_state)
    # explored.add(initial_state)

    while not frontier.isEmpty():
        current_state = frontier.pop()
        explored.add(current_state)

        if current_state == winningState:
            # Find the path, write to the output file,...
            return back_trace_dfs(parents, initial_state)

        # Create neighbors list of the current states, the return value needs to follow the rule UDLR
        # Add to stack in the order of RLDU in order to pop with the right order UDLR
        list_neighbors = find_neighbors(current_state)[::-1]
        for neighbor in list_neighbors:
            # neighbor is a tuple with the form ("Up", "123456780"), so neighbor[1] is the state, neighbor[0] is
            # the direction to get to that state from the current state (from parents)
            if (not frontier.contains(neighbor[1])) and (neighbor[1] not in explored):
                frontier.push(neighbor[1])
                parents[neighbor[1]] = (current_state, neighbor[0])

    return []

    # Add the initial state into explored
    # Add the initial state into the frontier, frontier is a stack
    # While the frontier is not empty
        # Pop a state out from the current state
        # Add the current state to explored

        # Check whether the current state is equal to [0,1,2,3,4,5,6,7,8]
            # if true, then return success/back trace to find the path,....

        # Generate the list of neighbors of the current states
        # Loop over the list of neighbors
            # if the neighbor is neither in the frontier nor the explored list, then add to frontier


def find_neighbors(state):
    """
    Given a state, this method return a list of its neighbor states in the order of UDLR, the return list will have the form
    [("Up", [.....]), ("Down", [.....]), .....]
    :param state
    :return: 
    """
    neighbors = []
    zero_index = state.index("0")
    # Check for Up and Down move
    # Index with the condition 2 < index < 6 can move both up and down
    if zero_index > 2:
        # Can move up
        newState = state[:zero_index - 3] + "0" + state[zero_index - 3 + 1: zero_index] + state[zero_index - 3] + state[zero_index + 1:]
        neighbors.append(("Up", newState))
    if zero_index < 6:
        # Can move down
        newState = state[:zero_index] + state[zero_index + 3] + state[zero_index + 1: zero_index + 3] + "0" + state[zero_index + 3 + 1:]
        neighbors.append(("Down", newState))
    if zero_index % 3 >= 1:
        # Can move left:
        newState = state[:zero_index - 1] + "0" + state[zero_index - 1 + 1: zero_index] + state[zero_index - 1] + state[zero_index + 1:]
        neighbors.append(("Left", newState))
    if zero_index % 3 <= 1:
        # Can move right
        newState = state[:zero_index] + state[zero_index + 1] + "0" + state[zero_index + 1 + 1:]
        neighbors.append(("Right", newState))

    return neighbors


def back_trace_dfs(parents, initial_state):
    path = []
    current_state = winningState
    while current_state != initial_state:
        path.append(parents[current_state][1])
        current_state = parents[current_state][0]
    return path[::-1]


class StackFrontier(object):
    def __init__(self):
        self.stack = []
        self.setElements = set()

    def push(self, element):
        self.stack.append(element)
        self.setElements.add(element)

    def pop(self):
        ele = self.stack.pop()
        self.setElements.remove(ele)
        return ele

    def isEmpty(self):
        return len(self.stack) == 0

    def contains(self, element):
        return element in self.setElements

main()
