
class Pedido:
  def __init__(self, cliente, restaurante, prato, entregador, qntPedido=1):
    self.cliente = cliente
    self.restaurante = restaurante
    self.prato = prato
    self.entregador = entregador
    self.qntPedido = qntPedido
    