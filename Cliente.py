from Restaurante import Restaurante
from Prato import Prato

class Cliente:

    def __init__(self, n, b, t):
        self.nome = n
        self.bairro = b
        self.telefone = t

    def getNome(self):
        return self.nome

    def getBairro(self):
        return self.bairro

    def getTelefone(self):
        return self.telefone
    
    # o usuário faz 3 avaliações separadas
    # cada avaliação entra no array de avaliações de cada objeto
    # dentro dos objetos, é feita a média das avaliações dentro do array
    def avalia(pedido, restaurante, entregador):

        aRestaurante = float(input('Qual a sua avaliação do restaurante? (1 a 5)\n'))
        if (aRestaurante >= 1 and aRestaurante <= 5):
            restaurante.avaliacao.append(aRestaurante)

        aEntregador = float(input('Qual a sua avaliação do entregador? (1 a 5)\n'))
        if (aEntregador >= 1 and aEntregador <= 5):
            entregador.avaliacao.append(aEntregador)
    
    def pedirPrato(self, restaurante):
        '''restCliente = input("\nInsira o restaurante que queira pedir.\n(rest1, rest2, rest3, rest4) : ")
        pratoCliente = input("\nInsira o prato de escolhar")
        if prato:
            return prato.pedido
        else:
            return None
        '''
        restaurante.getCardapio()
        pratoEscolhido = input("\nSelecione um prato pelo nome: ")
        
        if restaurante.validarPrato(pratoEscolhido) is not False:
            return restaurante.validarPrato(pratoEscolhido)
        else:
            self.pedirPrato(restaurante)

