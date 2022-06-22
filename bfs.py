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

        for filho in no.filhos(self.problema):
            if (not self.fronteira in filho) and (not self.visitado(filho.estado)):
                self.fronteira.append(filho)
                self.visitados.append(filho.estado)
        

    def visitado(self, estado):
        return estado in self.visitados
    

    def mostraSolucao(self):
        return str(self.solucao) +  "\nCusto:" + str(self.solucao[len(self.solucao) - 1].custo)
    

    def mostraFronteira(self):
        return '[' + str(self.fronteira) + ']'
    
