from utils import *

class BuscaLargura:
    def __init__(self, problema):
        self.problema = problema
        self.fronteira = [problema.inicial]
        self.visitados = [problema.inicial.estado]
        self.situacao = BUSCA_INICIANDO
        self.solucao = []
    

    def efetuarBusca(self):
        while ((self.situacao != BUSCA_FALHA) and (self.situacao != BUSCA_SUCESSO)):
            self.passoBusca()
        

        if (self.situacao == BUSCA_FALHA):
            print("Busca falhou")
        else:
            print("Solucao encontrada: ")
            print(self.mostraSolucao())
        
    def passoBusca(self):
        if (self.situacao == BUSCA_FALHA):
            print("Busca falhou")
            return

        if (self.situacao == BUSCA_SUCESSO):
            print("Busca encontrou a solucao")
            return

        no = self.fronteira.pop(0)

        if (not no):
            self.situacao = BUSCA_FALHA
            return

        print('no atual: estado ' + str(no.estado) + ' - custo: ' + str(no.custo))

        if (self.problema.objetivo(no)):
            self.solucao = no.constroiSolucao()
            self.situacao = BUSCA_SUCESSO
            return
        print(self.fronteira)
        print("1")
        print(no.filhos(self.problema))
        for filho in no.filhos(self.problema):
            print("2")
            print(filho)
            if (not filho in self.fronteira):
                print(3)
                if not self.visitado(filho.estado):
                    self.fronteira.append(filho)
                    self.visitados.append(filho.estado)
            

    def visitado(self, estado):
        return self.visitados in estado
    

    def mostraSolucao(self):
        return " -> ".join(str(self.solucao)) +  "Custo:" + str(self.solucao[self.solucao.length - 1].custo)
    

    def mostraFronteira(self):
        return '[' + " ".join(str(self.fronteira)) + ']'
    
