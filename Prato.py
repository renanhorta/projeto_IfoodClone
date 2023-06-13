class Prato:
  def __init__(self,nome,tipoDePrato,preco,quantidade,qntServe=2):
    self.nome = nome
    self.tipoDePrato = tipoDePrato
    self.preco = preco
    self.quantidadeVendida = quantidade
    #  Serve quantas pessoas. padrão vai ser 2 pessoas por cada prato.
    self.quantoServe = qntServe

  def getNome(self):
    return self.nome
  
  def getPreco(self):
    return self.preco * self.quantidadeVendida

  def quantosServem(self):
    return self.quantoServe

  def getTipoDePrato(self):
    return self.tipoDePrato
  
  def temAlergia(self, tipoDePrato):
    if tipoDePrato == "frutos do mar":
      return "Pode conter tropomiosina, Atenção alergicos a frutos do mar!"
    elif tipoDePrato == "gluten" or tipoDePrato == "lactose":
      return "Pode conter glúten ou lactose. Atenção celiacos!"
    elif tipoDePrato == "vegetariano"
      return "Prato vegetáriano, não contém proteina animal"
    elif tipoDePrato == "vegano"
      return "Prato vegano, não contém produtos de origem animal"
    else:
      return "Prato com produtos de origem animal e outros tipos de alimentos."
  
    #talvez criar um metodo com a descrição do que é o prato. Usar uma lista para
    #guardar os tipos de prato e usar o metodo
    

