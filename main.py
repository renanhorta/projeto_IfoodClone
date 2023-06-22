from Restaurante import Restaurante
from Cliente import Cliente

'''
c1 = Cliente('Juli', 'Botafogo', 21975707058)
r1 = Restaurante('Mizu', 'Botafogo', 'Japonesa', 5)
e1 = Entregador('Zé', 'Moto', 'Botafogo')
pr1 = Prato('Yakissoba de Legumes', 'gluten', 19.99, 1, 1)
p1 = Pedido(c1, r1, pr1, e1)

print(p1.entregador.valorReceber(pr1, r1))

p1.cliente.avalia(r1, e1)
p1.cliente.avalia(r1, e1)

print(r1.getAvaliacao())
print(e1.getAvaliacao())

print(r1.avaliacao)
print(e1.avaliacao)
'''

#criar os restaurantes no sistema

rest1= Restaurante("Bar da Hlera", "ramos", "brasileira", 9)
#rest2= Restaurante("aquele_outro", "ramos", "japonesa", 12)

# criar os cardapios de cada restaurante

rest1.criarCardapio()
#rest2.criarCardapio()

#criar os clientes

cli1 = Cliente("renan", "bonsucesso", "333333")
#cli2 = Cliente("Juli", "botafogo", "222222")

#mostar o cardapio e o cliente fazer o pedido

rest1.validarPrato(cli1.pedirPrato(rest1))
#rest2.validarPrato(cli2.pedirPrato(rest2))

#confirmar o pedido

#Criar o Entregador
