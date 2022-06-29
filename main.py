from algorithms.bfs import *
from algorithms.dfs import *
from algorithms.astar import *
from problems.romenia import *
from problems.aspirador import *
from sys import argv

'''
    Grupo:
        Caio Lucas da Silva Chacon
        Guilherme Iram Silva Araújo
        Luiz Fernando Costa dos Santos
'''

if len(argv) == 1:
    argv.append("Arad")

print(f"\nRomania route problem - {argv[1].strip().title()}")

initial_node = Node(argv[1].strip().title(), 0, None, None, euclidean_heuristic_dict[argv[1].strip().title()]);
romania_problem = Problem(initial_node, (lambda no: no if no.state == 'Bucharest' else None), romania_states)
ba = A_star(romania_problem)

if argv[1] == "Arad":
    print("\nA* search - step by step\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print("-"*150)
    print("\nA* search - solution\n")
    ba.search()

elif argv[1] == "Lugoj":
    print("\nA* search - step by step\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print("-"*150)
    print("\nA* search\n")
    ba.search()

elif argv[1] == "Neamt":
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print(ba.show_frontier(), "\n")
    ba.search_step()
    print("-"*150)
    print("\nA* search\n")
    ba.search()
else:
    print("\nA* search\n")
    ba.search()




