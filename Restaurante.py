from Prato import Prato
class Restaurante:

    def __init__(self, n, b, c, t):
        self.nome = n
        self.bairro = b
        self.cozinha = c
        self.taxaDeEntrega = t
        self.avaliacao = []
        self.avaliacaoMedia = 0
        self.cardapio = []

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
    
    # pesquisar melhor forma de criar um cardapio para o restaurante, o que vai ter para entregar e ver se vale azer um dicionário com prato e alergia
    def criarCardapio(self):
        
        while True:
            prato = input("\nCaso queria sair do menu digite '0' e 'enter' para continuar: ")
            if prato != '0':
                self.criarPrato()
            else:
                break

    def criarPrato(self):
        nomePrato = input("\nInsira o nome do prato: ")
        tipoDePrato = input("\nInsira o tipo de alimento que tem no prato\n(frutos do mar, gluten, vegetariano, vegano, outros ): ")
        preco = float(input("\nInsira o valor do prato: "))
        #mudar esse metodo no obj prato. O prato precisa ter um "estoque" e o cliente precisa pedir um valor aceitavel
        quantidade = int(input("Insira a quantidade: "))
        qntServe = int(input("\nQuantas pessoas o prato serve: "))
        prato = Prato(nomePrato, tipoDePrato, preco, quantidade, qntServe)
        
        return self.cardapio.append(prato)
        
        #ver uma forma de alinhar os dados do prato para apresentar um cardapio para o cliente.
        # (nome do prato) (preço) (quantidadeDisponivel) (quantos servem)  
        # cliente vai pedir pelo nome do prato e vai finalizar o pedido.   

    def getCardapio(self):
        saida = ""
        for prato in self.cardapio:
            saida += f"{prato.getNome()} - {prato.getPreco():.2f} - {prato.getTipoDePrato()} - {prato.quantosServem()}\n"
        return print(saida)
    
    def validarPrato(self, pratoEscolhido):
        for prato in  self.cardapio:
            if prato.getNome() == pratoEscolhido:
                return True
            else:
                print("Escolha um prato disponivel.")
                return False
    
    def getPrato(self, pratoEscolhido):
        for prato in  self.cardapio:
            if prato.getNome() == pratoEscolhido:
                saida = f"\nPEDIDO CONFIRMADO\nSeu prato é: {prato.getNome()} \n{prato.temAlergia(prato.getTipoDePrato)} \nO valor é de : R${prato.getPreco():.2f} \nE serve até {prato.quantosServem()} pessoas."
                print(saida)
