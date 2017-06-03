import sys
import time
import resource
import queue
import heapq

winningState = "012345678"
indexTable = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8}
indexRow = {0: 1, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3}

def main():
    # search_type = sys.argv[1]
    # initial_state = sys.argv[2].translate(str.maketrans({",": ""}))
    #
    # result = []
    # if search_type == "dfs":
    #     result = dfs_solution(initial_state)
    # elif search_type == "bfs":
    #     result = bfs_solution(initial_state)
    # else:
    #     result = ast_solution(initial_state)

    # print(dfs_solution(initial_state))
    # print(bfs_solution(initial_state))
    # print(resource.getrusage(resource.RUSAGE_SELF))

    # print(heuristic("753124680"))
    print(dfs_solution("567801234"))
    print(bfs_solution("567801234"))
    print(ast_solution("567801234"))


    # print(heuristic("618042735"))
    # checkHeuristic()
    # checkSearchs()
    # showResults(result)


def showResults(result):
    print("path_to_goal: "+str(result[0]))
    print("cost_of_path: "+str(len(result[0])))
    print("nodes_expanded: "+str(result[2]))
    print("search_depth: "+str(len(result[0])))
    print("max_search_depth: "+str(result[1]))
    print("running_time: "+str(resource.getrusage(resource.RUSAGE_SELF).ru_utime))
    print("max_ram_usage: "+str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024)))



def checkHeuristic():
    assert heuristic("123456780") == 12
    assert heuristic("146823075") == 14
    assert heuristic("543782106") == 17
    assert heuristic("618402735") == 10

    print("All tests passed!")


def checkSearchs():
    # assert bfs_solution("567801234")[0] == ast_solution("567801234")[0]

    assert bfs_solution("123456780")[0] == ast_solution("123456780")[0]
    assert bfs_solution("146823075")[0] == ast_solution("146823075")[0]
    assert bfs_solution("543782106")[0] == ast_solution("543782106")[0]
    assert bfs_solution("618402735")[0] == ast_solution("618402735")[0]
    assert bfs_solution("864213570")[0] == ast_solution("864213570")[0]
    # assert bfs_solution("453216780")[0] == ast_solution("453216780")[0]
    assert bfs_solution("012345678")[0] == ast_solution("012345678")[0]
    assert bfs_solution("125340678")[0] == ast_solution("125340678")[0]
    assert bfs_solution("753124680")[0] == ast_solution("753124680")[0]


    print("All test passed!!!")



def dfs_solution(initial_state):
    frontier = StackFrontier()
    explored = set()
    parents = {}
    # The element in frontier is (state, depth)
    frontier.push((initial_state, 0))

    maxDepth = 0
    while not frontier.isEmpty():
        current_state = frontier.pop()
        # Only add current state to explored, no need to add depth of that state
        explored.add(current_state[0])

        if current_state[0] == winningState:
            # Find the path, write to the output file,...
            path = back_trace(parents, initial_state)
            return [path, maxDepth, len(explored) - 1]

        # Create neighbors list of the current states, the return value needs to follow the rule UDLR
        # Add to stack in the order of RLDU in order to pop with the right order UDLR
        list_neighbors = find_neighbors(current_state[0])[::-1]
        for neighbor in list_neighbors:
            # neighbor is a tuple with the form ("Up", "123456780"), so neighbor[1] is the state, neighbor[0] is
            # the direction to get to that state from the current state (from parents)
            if (not frontier.contains(neighbor[1])) and (neighbor[1] not in explored):
                frontier.push((neighbor[1], current_state[1]+1))
                parents[neighbor[1]] = (current_state[0], neighbor[0])
                if current_state[1] + 1 > maxDepth:
                    maxDepth = current_state[1] + 1
    return []


def bfs_solution(initial_state):
    frontier = QueueFrontier()
    explored = set()
    parents = {}

    # Element in frontier is in from (state, depth)
    frontier.add((initial_state, 0))

    maxDepth = 0

    while not frontier.isEmpty():
        current_state = frontier.pop()
        explored.add(current_state[0])

        if current_state[0] == winningState:
            path = back_trace(parents, initial_state)
            return [path, maxDepth, len(explored) - 1]

        # Create a list of neighbors of the current state, the return value follows the rule UDLR
        list_neighbors = find_neighbors(current_state[0])
        for neighbor in list_neighbors:
            # neighbor is a tuple ("Up", "123456780")
            if (not frontier.contains(neighbor[1])) and (neighbor[1] not in explored):
                frontier.add((neighbor[1], current_state[1] + 1))
                parents[neighbor[1]] = (current_state[0], neighbor[0])
                if current_state[1] + 1 > maxDepth:
                    maxDepth = current_state[1] + 1
    return []


def ast_solution(initial_state):
    # The smaller the score, the higher priority
    scoreDirection = {"Up": 1, "Down": 2, "Left": 3, "Right": 4}

    frontier = PriorityQueueFrontier()
    explored = set()
    parents = {}

    # Frontier is a priority queue that take a tuple as element, (ManhattanScore, directionScore, state, depth)
    frontier.add((0, 0, initial_state, 0))
    maxDepth = 0

    while not frontier.isEmpty():
        current_state = frontier.pop(explored)

        explored.add(current_state[2])

        if current_state[2] == winningState:
            path = back_trace(parents, initial_state)
            return [path, maxDepth, len(explored) - 1]

        list_neighbors = find_neighbors(current_state[2])

        for neighbor in list_neighbors:
            depth = current_state[3] + 1
            if (not frontier.contains(neighbor[1])) and (neighbor[1] not in explored):
                frontier.add((heuristic(neighbor[1]) + depth, scoreDirection[neighbor[0]], neighbor[1], depth))
                parents[neighbor[1]] = (current_state[2], neighbor[0])
                if depth > maxDepth:
                    maxDepth = depth
            elif frontier.contains(neighbor[1]) and (neighbor[1] not in explored):
                if frontier.get(neighbor[1]) > heuristic(neighbor[1]) + depth:
                    frontier.add((heuristic(neighbor[1]) + depth, scoreDirection[neighbor[0]], neighbor[1], depth))
                    parents[neighbor[1]] = (current_state[2], neighbor[0])
                    if depth > maxDepth:
                        maxDepth = depth
    return []


def find_neighbors(state):
    """
    Given a state, this method return a list of its neighbor states in the order of UDLR, the return list will have the form
    [("Up", [.....]), ("Down", [.....]), .....]
    :param state
    :return: List of neighbors of the input state in the form of ("Up", "123456780")
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


def back_trace(parents, initial_state):
    path = []
    current_state = winningState
    while current_state != initial_state:
        path.append(parents[current_state][1])
        current_state = parents[current_state][0]
    return path[::-1]


def heuristic(state):
    """
    Method to find the heuristic score (Manhattan distance score) of the given state 
    :param state: the input state to calculate its Manhattan score
    :return: The Manhattan distance score of the input state
    """
    # Loop through each index of the input
    # For each index:
    #   If the tile value is 0, then skip
    #   Else, calculate the score of a tile as below:
    #       Look up the true index of the tile from the reference dictionary
    #       Manhattan distance += abs(trueIndex%3 - currentIndex%3) + abs(indexRow[trueIndex] - indexRow[currentIndex])
    # The reason: difference // 3 will tell us how far to move vertical, difference % 3 will tell us how far to move horizontal
    manhattanDistance = 0
    for i in range(len(state)):
        if state[i] == "0":
            pass
        else:
            trueIndex = indexTable[state[i]]
            manhattanDistance += abs(trueIndex % 3 - i % 3) + abs(indexRow[trueIndex] - indexRow[i])
    return manhattanDistance

class StackFrontier(object):
    """
    This is the class of implementation for a Stack used with DFS solution. This implementation will guarantee a O(1) time
    complexity on both checking membership and adding/removing element from the stack.
    The membership checking is done by using a set data structure underneath.
    """
    def __init__(self):
        # Element in stack is in form (state, depth), element in setElements is only state
        self.stack = []
        self.setElements = set()

    def push(self, element):
        self.stack.append(element)
        self.setElements.add(element[0])

    def pop(self):
        ele = self.stack.pop()
        self.setElements.remove(ele[0])
        return ele

    def isEmpty(self):
        return len(self.stack) == 0

    def contains(self, element):
        return element in self.setElements


class QueueFrontier(object):
    def __init__(self):
        self.frontier = queue.Queue()
        self.setElements = set()

    def add(self, element):
        self.frontier.put_nowait(element)
        self.setElements.add(element[0])

    def pop(self):
        ele = self.frontier.get_nowait()
        self.setElements.remove(ele[0])
        return ele

    def isEmpty(self):
        return self.frontier.empty()

    def contains(self, element):
        return element in self.setElements


class PriorityQueueFrontier(object):
    def __init__(self):
        self.frontier = queue.PriorityQueue()
        self.dictElements = {}

    def add(self, element):
        self.frontier.put_nowait(element)
        self.dictElements[element[2]] = element[0]

    def pop(self, explored):
        # Get the first element in the priority queue, and remove it from the set element
        ele = self.frontier.get_nowait()
        while not self.contains(ele[2]):
            ele = self.frontier.get_nowait()
        del self.dictElements[ele[2]]
        return ele

    def get(self, element):
        return self.dictElements[element]

    def isEmpty(self):
        return len(self.dictElements) == 0

    def contains(self, element):
        return element in self.dictElements


class HeapFrontier(object):
    def __init__(self):
        self.frontier = []
        self.dictElements = {}

    def add(self, element):
        if self.contains(element[1]):
            old = ()
            for ele in self.frontier:
                if ele[1] == element[1]:
                    old = ele
                    break
            self.frontier.remove(old)
            self.frontier.append(element)
        else:
            self.frontier.append(element)
        self.dictElements[element[1]] = element[0]

    def pop(self):
        # Get the first element in the priority queue, and remove it from the set element
        ele = heapq.heappop(self.frontier)
        del self.dictElements[ele[1]]
        return ele

    def get(self, element):
        return self.dictElements[element]

    def isEmpty(self):
        return len(self.dictElements) == 0

    def contains(self, element):
        return element in self.dictElements



main()
