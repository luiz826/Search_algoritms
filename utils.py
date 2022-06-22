# constantes para situacao atual da busca
BUSCA_INICIANDO = 0
BUSCA_EM_CURSO = 1
BUSCA_FALHA = 2
BUSCA_SUCESSO = 3

class No:
    def __init__(self, estado, custo, pai, acao):
        self.estado = estado
        self.custo = custo
        self.pai = pai
        self.acao = acao

    def __iter__(self):
        return iter(f"({self.estado}, {self.custo})")

    def __repr__(self) -> str():
        return f"({self.estado}, {self.custo})"

    def filhos(self, problema):
        estado_acoes = list(map(lambda ea: ea if self.estado == ea["estado"] else None, problema.espacoEstados))
        
        estado_acoes = list(filter(None, estado_acoes))
        if (not estado_acoes):
            return []

        resultado = []
        for acao in estado_acoes[0]["acoes"]:
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