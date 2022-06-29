from algorithms.utils import *
from algorithms.search import *

class A_star(Search):
    def __init__(self, problem):
        super().__init__(problem)
        self.frontier =  PriorityQueue(problem.initial)
                
    def search_step(self):
        if (self.situation == FAIL_SEARCH):
            print("Fail Search")
            return

        if (self.situation == SUCCESS_SEARCH):
            print("Search find a solution")
            return

        node = self.frontier.pop_()

        if (not node):
            self.situation = FAIL_SEARCH
            return

        print('Actual node: State ' + str(node.state) + ' - Cost: ' + str(node.cost) +\
              ' - Cost+Heuristic: ' + str(node.heuristic+node.cost))
        if (self.problem.objective(node)):
            self.solution = node.build_solution()
            self.situation = SUCCESS_SEARCH
            return

        for child in node.children(self.problem):
            if (not self.frontier in child):
                self.frontier.insert(child)        
