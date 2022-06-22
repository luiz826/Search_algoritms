from bfs import *
from dfs import *
from romenia import *
from aspirador import *

no_inicial = No([0,0,0], 1, None, None)
problemaAspirador = Problema(no_inicial, (lambda no: no if no.estado == [1,1,1] else None), estadosAspirador)

# bl = BuscaLargura(problemaAspirador)
# bl.efetuarBusca()

bp = BuscaProfundidade(problemaAspirador)
bp.efetuarBusca()

# no_arad = No('Arad', 0, None, None);

# problemaRomenia = Problema(no_arad, (lambda no: no if no.estado == 'Bucharest' else None), estadosRomenia)

# bl = BuscaLargura(problemaRomenia)
# bp = BuscaProfundidade(problemaRomenia)

# print("\nBusca em Largura\n")
# bl.efetuarBusca()
# print("\nBusca em Profundidade\n")
# bp.efetuarBusca()