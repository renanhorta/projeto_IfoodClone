from Prato import Prato
from Restaurante import Restaurante
from Cliente import Cliente
from Entregador import Entregador

class Pedido:
  def __init__(self, cliente, restaurante, prato, entregador):
    self.cliente = cliente
    self.restaurante = restaurante
    self.prato = prato 
    self.entregador = entregador

c1 = Cliente('Juli', 'Botafogo', 21975707058)
r1 = Restaurante('Mizu', 'Botafogo', 'Japonesa', 5)
e1 = Entregador('Zé', 'Moto', 'Botafogo')
pr1 = Prato('Yakissoba de Legumes', 'gluten', 19.99, 1, 1)
p1 = Pedido(c1, r1, pr1, e1)

print(p1.entregador.valorReceber(pr1, r1))