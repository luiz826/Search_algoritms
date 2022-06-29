class Node:
    def __init__(self, state, cost, parent, action, heuristic=None):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.action = action
        self.heuristic = heuristic

    def __iter__(self):
        return iter(f"({self.state}, {self.cost})")

    def __repr__(self) -> str():
        if self.heuristic != None:
            return f"({self.state}, {self.cost}, {self.heuristic}, {self.cost + self.heuristic})"
        return f"({self.state}, {self.cost})"

    def children(self, problem):
        for state_space in problem.state_space:
            if self.state.strip() == state_space["state"].strip():
                break
        
        if (not state_space):
            return []

        result = []
        for action in state_space["actions"]:
            newNode = Node(action["destiny"], self.cost + action["cost"], self,
                                action["destiny"], action["heuristic"])
            result.append(newNode)

        return result
    
    def build_solution(self):
        node = Node(self.state, self.cost, self.parent, self.action)
        solution = []

        while (node != None):
            solution.insert(0, node)  # add node in front of solution
            node = node.parent

        return solution

class Problem:
    def __init__(self, initial, objective, state_space):
        self.initial = initial
        self.objective = objective
        self.state_space = state_space

class PriorityQueue:
    def __init__(self, initial=None):
        self.queue = [initial]
    
    def __repr__(self):
        return ' '.join([str(i) for i in self.queue])
 
    def isEmpty(self):
        return len(self.queue) == 0
 

    def insert(self, data):
        self.queue.append(data)

    def pop_(self):
        try:
            min_val = len(self.queue) - 1
            for i in range(len(self.queue)):
                if (self.queue[i].cost + self.queue[i].heuristic) < (self.queue[min_val].cost + self.queue[min_val].heuristic):
                    min_val = i
            item = self.queue[min_val] 
            del self.queue[min_val]
            return item 
        except IndexError:
            print()
            exit()
        