class Restaurante:

    def __init__(self, n, b, c, t):
        self.nome = n
        self.bairro = b
        self.cozinha = c
        self.taxaDeEntrega = t
        self.avaliacao = []
        self.avaliacaoMedia = 0

    def getNome(self):
        return self.nome

    def getBairro(self):
        return self.bairro

    def getCozinha(self):
        return self.cozinha
        
    def getTaxa(self):
        return self.taxaDeEntrega
    
    # se o array de avaliações não estiver vazio,
    # todas as avaliações são somadas e divididas pelo número de avaliações (no caso, o tamanho do array de avaliações)
    # caso o array esteja vazio, retorna None
    def getAvaliacao(self):
        if self.avaliacao != []:
            for a in self.avaliacao:
                self.avaliacaoMedia += a
            return round(self.avaliacaoMedia/len(self.avaliacao), 2)
        else:
            return None
