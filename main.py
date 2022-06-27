from algorithms.bfs import *
from algorithms.dfs import *
from problems.romenia import *
from problems.aspirador import *

# PROBLEMA ASPIRADOR R3
no_inicial = No([0,0,0], 1, None, None)
problemaAspirador = Problema(no_inicial, (lambda no: no if no.estado == [1,1,1] else None), estadosAspirador)

bl = BuscaLargura(problemaAspirador)
bp = BuscaProfundidade(problemaAspirador)
print("\nBusca em Largura\n")
bl.efetuarBusca()
print("\nBusca em Profundidade\n")
bp.efetuarBusca()

# PROBLEMA ASPIRADOR R4
no_inicial = No([0,0,0,0], 1, None, None)
problemaAspirador = Problema(no_inicial, (lambda no: no if no.estado == [1,1,1,1] else None), estadosAspirador2)

bl = BuscaLargura(problemaAspirador)
bp = BuscaProfundidade(problemaAspirador)
print("\nBusca em Largura\n")
bl.efetuarBusca()
print("\nBusca em Profundidade\n")
bp.efetuarBusca()

# PROBLEMA ROTA ROMENIA
no_arad = No('Arad', 0, None, None);

problemaRomenia = Problema(no_arad, (lambda no: no if no.estado == 'Bucharest' else None), estadosRomenia)

bl = BuscaLargura(problemaRomenia)
bp = BuscaProfundidade(problemaRomenia)
print("\nBusca em Largura\n")
bl.efetuarBusca()
print("\nBusca em Profundidade\n")
bp.efetuarBusca()
