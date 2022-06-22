from bfs import *

no_arad = No('Arad', 0, None, None);

problemaRomenia = Problema(no_arad, (lambda no: no if no.estado == 'Bucharest' else None), estadosRomenia)


