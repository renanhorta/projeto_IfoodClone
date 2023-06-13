class Entregador:
  def __init__(self, nome, veiculo, local):
    self.nome = nome
    self.veiculo = veiculo
    self.local = local
    self.aEntregador = []

  def getNome(self):
    return self.nome

  def getVeiculo(self):
    return self.veiculo

  def getLocal(self):
    return self.local

  def valorReceber(self, prato, restaurante):
    txEntrega = (prato.getPreco()) + (restaurante.getTaxa()) * 0.13
    return round(txEntrega, 2)

  #Metodo para atualzar o local do entregador( nesse projeto será atualizado na hora de pegar o prato
  #e na hora de chegar próximo no cliente, provalvelmente na rua.)
  def atualizaLocal(self):
    novoLocal = print("Informe o seu novo local")
    return novoLocal

  