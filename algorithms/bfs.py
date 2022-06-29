from algorithms.search import *

class Breadth_first(Search):
    def __init__(self, problem):
        super().__init__(problem)
        self.frontier = [problem.initial]
        
    def search_step(self):
        if (self.situation == FAIL_SEARCH):
            print("Fail Search")
            return

        if (self.situation == SUCCESS_SEARCH):
            print("Search find a solution")
            return

        node = self.frontier.pop(0)

        if (not node):
            self.situation = FAIL_SEARCH
            return

        print('Actual node: State ' + str(node.state) + ' - Cost: ' + str(node.cost))

        if (self.problem.objective(node)):
            self.solution = node.build_solution()
            self.situation = SUCCESS_SEARCH
            return

        for child in node.children(self.problem):
            if (not self.frontier in child) and (not self.is_visited(child.state)):
                self.frontier.append(child)
                self.visited.append(child.state)
