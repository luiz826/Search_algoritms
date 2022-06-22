# constantes para situacao atual da busca
BUSCA_INICIANDO = 0
BUSCA_EM_CURSO = 1
BUSCA_FALHA = 2
BUSCA_SUCESSO = 3

# funcao auxiliar criada para ajudar a especificar "acoes"
def acao(destino, custo):
    return {"destino": destino, 
            "custo": custo}

estadosRomenia = [
    {
        "estado": 'Arad',
        "acoes": [ acao('Zerind', 75), acao('Sibiu', 140), acao('Timisoara', 118) ]
    },

    {
        "estado": 'Zerind',
        "acoes": [ acao('Arad', 75), acao('Oradea', 71) ]
    },

    {
        "estado": 'Timisoara',
        "acoes": [ acao('Arad', 118), acao('Lugoj', 111) ]
    },

    {
        "estado": 'Sibiu',
        "acoes": [ acao('Arad', 140), acao('Oradea', 151), acao('Fagaras', 99),
                 acao('Rimnicu Vilcea', 80)]
    },

    {
        "estado": 'Oradea',
        "acoes": [ acao('Zerind', 71), acao('Sibiu', 151) ]
    },

    {
        "estado": 'Lugoj',
        "acoes": [ acao('Timisoara', 111), acao('Mehadia', 70) ]
    },

    {
        "estado": 'Mehadia',
        "acoes": [ acao('Lugoj', 70), acao('Drobeta', 75) ]
    },

    {
        "estado": 'Drobeta',
        "acoes": [ acao('Mehadia', 75), acao('Craiova', 120) ]
    },

    {
        "estado": 'Craiova',
        "acoes": [ acao('Drobeta', 120), acao('Rimnicu Vilcea', 146), acao('Pitesti', 138) ]
    },

    {
        "estado": 'Rimnicu Vilcea',
        "acoes": [ acao('Sibiu', 80), acao('Craiova', 146), acao('Pitesti', 97) ]
    },

    {
        "estado": 'Fagaras',
        "acoes": [ acao('Sibiu', 99), acao('Bucharest', 211) ]
    },

    {
        "estado": 'Pitesti',
        "acoes": [ acao('Rimnicu Vilcea', 97), acao('Craiova', 138), acao('Bucharest', 101) ]
    },

    {
        "estado": 'Giurgiu',
        "acoes": [ acao('Bucharest', 90) ]
    },

    {
        "estado": 'Bucharest',
        "acoes": [ acao('Fagaras', 211), acao('Pitesti', 101), acao('Giurgiu', 90),
                 acao('Urziceni', 85) ]
    },

    {
        "estado": 'Urziceni',
        "acoes": [ acao('Bucharest', 85), acao('Vaslui', 142), acao('Hirsova', 98) ]
    },

    {
        "estado": 'Hirsova',
        "acoes": [ acao('Urziceni', 98), acao('Eforie', 86) ]
    },

    {
        "estado": 'Eforie',
        "acoes": [ acao('Hirsova', 86) ]
    },

    {
        "estado": 'Vaslui',
        "acoes": [ acao('Urziceni', 142), acao('Iasi', 92) ]
    },

    {
        "estado": 'Iasi',
        "acoes": [ acao('Vaslui', 92), acao('Neamt', 87) ]
    },

    {
        "estado": 'Neamt',
        "acoes": [ acao('Iasi', 87) ]
    }
]

class No:
    def __init__(self, estado, custo, pai, acao):
        self.estado = estado
        self.custo = custo
        self.pai = pai
        self.acao = acao

    def __repr__(self) -> str():
        return f"({self.estado}, {self.custo})"

    def filhos(self, problema):
        estado_acoes = list(map(lambda ea: ea if self.estado == ea["estado"] else None), problema.espacoEstados)
        print(estado_acoes)
        if (not estado_acoes):
            return []

        resultado = []
        for acao in estado_acoes["acoes"]:
            novoNo = No(acao["destino"], self.custo + acao["custo"], self,
                                acao["destino"])
            resultado.append(novoNo)
        

        return resultado
    
    def constroiSolucao(self):
        no = No(self.estado, self.custo, self.pai, self.acao)
        solucao = []

        while (no != None):
            solucao.insert(0, no)  # adiciona no na frente da solucao
            no = no.pai
        
        return solucao
    
class Problema:
    def __init__(self, inicial, objetivo, espacoEstados):
        self.inicial = inicial
        self.objetivo = objetivo
        self.espacoEstados = espacoEstados
    
