from problems.utils import *

# Constants for situation in search
STARTING_SEARCH = 0
ONGOING_SEARCH = 1
FAIL_SEARCH = 2
SUCCESS_SEARCH = 3

class Search:
    def __init__(self, problem):
        self.problem = problem
        self.visited = [problem.initial.state]
        self.situation = STARTING_SEARCH
        self.solution = []

    def search(self):
        while ((self.situation != FAIL_SEARCH) and (self.situation != SUCCESS_SEARCH)):
            self.search_step()
        
        if (self.situation == FAIL_SEARCH):
            print("Fail Search")
        else:
            print("Find Solution: ")
            print(self.show_solution())

    def is_visited(self, state):
        return state in self.visited

    def show_solution(self):
        return str(self.solution) + "\nCost:" + str(self.solution[len(self.solution) - 1].cost)
