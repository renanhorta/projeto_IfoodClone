class Entregador:
  def __init__(self, nome, veiculo, local):
    self.nome = nome
    self.veiculo = veiculo
    self.local = local
    self.avaliacao = []
    self.avaliacaoMedia = 0

  def getNome(self):
    return self.nome

  def getVeiculo(self):
    return self.veiculo

  def getLocal(self):
    return self.local

  def valorReceber(self, prato, restaurante):
    txEntrega = (prato.getPreco_final()) + (restaurante.getTaxa()) * 0.13
    return round(txEntrega, 2)

  #Metodo para atualzar o local do entregador( nesse projeto será atualizado na hora de pegar o prato
  #e na hora de chegar próximo no cliente, provalvelmente na rua.)
  def atualizaLocal(self):
    novoLocal = print("Informe o seu novo local")
    return novoLocal
  
  # se a lista de avaliações não estiver vazio,
  # todas as avaliações são somadas e divididas pelo número de avaliações (no caso, o tamanho da lista de avaliações)
  # caso a lista esteja vazio, retorna None
  def getAvaliacao(self):
      if self.avaliacao != []:
          for a in self.avaliacao:
              self.avaliacaoMedia += a
          return round(self.avaliacaoMedia/len(self.avaliacao), 2)
      else:
          return None

  