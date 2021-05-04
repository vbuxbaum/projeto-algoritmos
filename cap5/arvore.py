''' Implementação de Arvore Binária com Programação Orientada a Objetos '''


class No:
    '''Um Nó de Árvore binária tem duas ligações.'''

    def __init__(self, valor):
        self.valor = valor
        self.no_esquerdo = None
        self.no_direito = None


class ArvoreBinaria:
    '''Uma Árvore Binária é uma estrutura de dados composta de nós com 2 
    filhos conectados unidirecionalmente'''

    def __init__(self):
        self.no_raiz = None



    def insere(self, no):
        antecessor = None
        no_atual = self.no_raiz

        while no_atual:
            antecessor = no_atual
            if no < no_atual:
                no_atual = no_atual.no_esquerdo
            else:
                no_atual = no_atual.no_direito
                
        if no.valor > antecessor.valor:
            antecessor.no_direito = no
        else:
            antecessor.no_esquerdo = no

        no_atual = no

    def retira(self, no):



if __name__ == "__main__":
    conjunto = [1, 2, 3, 4, 5, 6, 10, 54, -1, -67]
    assert True
