import sys

winningState = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


def main():
    search_type = sys.argv[1]
    initial_state = sys.argv[2].split(",")

    print(initial_state)


def dfs_solution(initial_state):
    frontier = StackFrontier()
    explored = set()

    frontier.push(initial_state)
    explored.add(initial_state)

    while not frontier.isEmpty():
        current_state = frontier.pop()
        explored.add(current_state)

        if current_state == winningState:
            # Find the path, write to the output file,...
            return ...

        # Create neighbors list of the current states, the return value needs to follow the rule UDLF
        # Add to stack in the order of FLDU in order to pop with the right order UDLF
        list_neighbors = find_neighbors(current_state)[::-1]
        for neighbor in list_neighbors:
            if not frontier.contains(neighbor) and neighbor not in explored:
                frontier.push(neighbor)

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
    Given a state, this method return a list of its neighbor states in the order of UDLR
    :param state
    :return: 
    """
    # Make sure to create a copy of the input state to prevent modifying the input, since list in python is referenced
    state = state[::]
    neighbors = []
    zero_index = state.index("0")
    # Check for Up and Down move
    # Index with the condition 2 < index < 6 can move both up and down
    if zero_index > 2:
        # Can move up
        newState = state[::]
        newState[zero_index] = newState[zero_index - 3]
        newState[zero_index - 3] = "0"
        neighbors.append(newState)
    if zero_index < 6:
        # Can move down
        newState = state[::]
        newState[zero_index] = newState[zero_index + 3]
        newState[zero_index + 3] = "0"
        neighbors.append(newState)






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
