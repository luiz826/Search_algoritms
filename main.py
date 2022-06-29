from algorithms.bfs import *
from algorithms.dfs import *
from algorithms.astar import *
from problems.romenia import *
from problems.aspirador import *

#Vacuum Cleaner problem R^3
initial_node = Node([0,0,0], 1, None, None, 1)
vacuum_cleaner_problem = Problem(initial_node, (lambda no: no if no.state == [1,1,1] else None), vacuum_states)
print("\nVacuum Cleaner problem R^3\n")
bl = Breadth_first(vacuum_cleaner_problem)
bp = Depth_first(vacuum_cleaner_problem)
ba = A_star(vacuum_cleaner_problem)
print("\nBreadth-first search\n")
bl.search()
print("\nDepth-first Search\n")
bp.search()
print("\nA* search\n")
ba.search()

#Vacuum Cleaner problem R^4
initial_node = Node([0,0,0,0], 1, None, None, 1)
vacuum_cleaner_problem = Problem(initial_node, (lambda no: no if no.state == [1,1,1,1] else None), vacuum_states2)
print("\nVacuum Cleaner problem R^4\n")
bl = Breadth_first(vacuum_cleaner_problem)
bp = Depth_first(vacuum_cleaner_problem)
ba = A_star(vacuum_cleaner_problem)
print("\nBreadth-first search\n")
bl.search()
print("\nDepth-first Search\n")
bp.search()
print("\nA* search\n")
ba.search()

#Romania route problem 
arad_node = Node('Arad', 0, None, None, 366);
romania_problem = Problem(arad_node, (lambda no: no if no.state == 'Bucharest' else None), romania_states)
print("\nRomania route problem \n")
bl = Breadth_first(romania_problem)
bp = Depth_first(romania_problem)
ba = A_star(romania_problem)
print("\nBreadth-first search\n")
bl.search()
print("\nDepth-first Search\n")
bp.search()
print("\nA* search\n")
ba.search()

