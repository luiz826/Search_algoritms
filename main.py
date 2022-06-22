from bfs import *
from dfs import *

no_arad = No('Arad', 0, None, None);

problemaRomenia = Problema(no_arad, (lambda no: no if no.estado == 'Bucharest' else None), estadosRomenia)

bl = BuscaLargura(problemaRomenia)
bp = BuscaProfundidade(problemaRomenia)

print("\nBusca em Largura\n")
bl.efetuarBusca()
print("\nBusca em Profundidade\n")
bp.efetuarBusca()