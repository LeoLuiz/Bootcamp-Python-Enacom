from math import *
from enum import Enum
import random
import time

class Risco(Enum):
  BAIXO = 0
  MEDIO = 1
  ALTO = 2

class Investimento:
  """
  Classe que representa um investimento
  """

  def __init__(self, descricao:str, custo: float, retorno:float, risco: Risco):
    self.descricao = descricao
    self.custo = custo
    self.retorno = retorno
    self.risco = risco
  
  @property
  def retorno_relativo(self):
    return self.retorno/self.custo

  def __repr__(self):
    return f"({self.descricao}, R$ {self.custo})"


lista_de_investimentos = [
    {"descricao": "Ampliação da capacidade do armazém ZDP em 5%",
     "custo": 470_000,
     "retorno":410_000,
     "risco": Risco.BAIXO},

     {"descricao": "Ampliação da capacidade do armazém MGL em 7%",
     "custo": 400_000,
     "retorno":330_000,
     "risco": Risco.BAIXO},

     {"descricao": "Compra de empilhadeira",
     "custo": 170_000,
     "retorno":140_000,
     "risco": Risco.MEDIO},

     {"descricao": "Projeto de P&D I",
     "custo": 270_000,
     "retorno":250_000,
     "risco": Risco.MEDIO},

     {"descricao": "Projeto de P&D II",
     "custo": 340_000,
     "retorno":320_000,
     "risco": Risco.MEDIO},

     {"descricao": "Aquisição de novos equipamentos",
     "custo": 230_000,
     "retorno":320_000,
     "risco": Risco.MEDIO},

     {"descricao": "Capacitação de funcionários",
     "custo": 50_000,
     "retorno":90_000,
     "risco": Risco.MEDIO},

     {"descricao": "Ampliação da estrutura de carga rodoviária",
     "custo": 440_000,
     "retorno":190_000,
     "risco": Risco.ALTO},

     {"descricao": "Construção de datacenter",
     "custo": 320_000,
     "retorno":120_000,
     "risco": Risco.ALTO},

     {"descricao": "Aquisição de empresa concorrente",
     "custo": 800_000,
     "retorno":450_000,
     "risco": Risco.ALTO},

     {"descricao": "Compra de serviços em nuvem",
     "custo": 120_000,
     "retorno":80_000,
     "risco": Risco.BAIXO},

     {"descricao": "Criação de aplicativo mobile e desktop",
     "custo": 150_000,
     "retorno":120_000,
     "risco": Risco.BAIXO},

     {"descricao": "Terceirização do serviço de otimização da logística",
     "custo": 300_000,
     "retorno":380_000,
     "risco": Risco.MEDIO},
]

investimentos = list()
for info in lista_de_investimentos:
  investimento = Investimento(**info)
  investimentos.append(investimento)

investimentos

teto_de_gastos_por_classe = {
    Risco.BAIXO: 1_200_000,
    Risco.MEDIO: 1_500_000,
    Risco.ALTO: 900_000
}

min_investimentos_por_classe = {
    Risco.BAIXO: 2,
    Risco.MEDIO: 2,
    Risco.ALTO: 1
}
teto_orcamento = 2_400_000

def calc_retorno_esperado(self,selecionados):
  return sum(investimento.retorno for investimento in selecionados)

def AdicionarInvestimentos(self,solucao_atual):
  selecionados = list()
  selecionados = solucao_atual
  for classe, teto in self.teto_de_gastos_por_classe.items():
      investimentos_dessa_classe = [investimento for investimento in self.investimentos if investimento.risco == classe]
      sorteiaInvestimento = random.randrange(0, len(investimentos_dessa_classe))
      if(investimentos_dessa_classe[sorteiaInvestimento] not in solucao_atual):
        selecionados.append(investimentos_dessa_classe[sorteiaInvestimento])
        custo_total_ate_o_momento = sum(investimento.custo for investimento in selecionados)
        custo_dessa_classe = sum(investimento.custo for investimento in selecionados if (investimento.risco == classe and investimento in selecionados))
        if (custo_total_ate_o_momento > self.teto_orcamento or custo_dessa_classe > teto):
          del(selecionados[-1])
  return solucao_atual

def TrocarInvestimentos(self, solucao_atual):
    selecionados = list()
    selecionados = solucao_atual 
    for classe, teto in self.teto_de_gastos_por_classe.items():
        investimentos_dessa_classe = [investimento for investimento in self.investimentos if investimento.risco == classe]
        investimentos_disponiveis = [investimento for investimento in investimentos_dessa_classe if investimento not in selecionados]
        if len(investimentos_disponiveis) == 0:
            continue
        sorteiaInvestimento = random.randrange(0, len(investimentos_disponiveis))
        for i in range(len(selecionados)):
            if selecionados[i].risco == classe:
                auxTroca = selecionados[i]
                selecionados[i] = investimentos_disponiveis[sorteiaInvestimento]
                custo_total_ate_o_momento = sum(investimento.custo for investimento in selecionados)
                custo_dessa_classe = sum(investimento.custo for investimento in selecionados if (investimento.risco == classe and investimento in selecionados))
                if (custo_total_ate_o_momento > self.teto_orcamento or custo_dessa_classe > teto):
                  selecionados[i] = auxTroca
                break
    return selecionados

def RVND(self,kmax, solucao_atual):
  bloqueado = []
  aux_Sol= solucao_atual
  aux_Retorno = calc_retorno_esperado(self,solucao_atual)
  k = 1
  while(k < kmax):
    estrutura = random.randrange(1, 3) 
    if (estrutura not in bloqueado):
      if(estrutura == 1):
        AdicionarInvestimentos(self,solucao_atual)
      elif(estrutura == 2):
        TrocarInvestimentos(self,solucao_atual)
        
      retornoAtual = calc_retorno_esperado(self,solucao_atual)
      if(retornoAtual < aux_Retorno):
        aux_Retorno = retornoAtual
        aux_Sol = solucao_atual
        bloqueado.clear()
      else:
        bloqueado.append(estrutura)
        solucao_atual = aux_Sol
        retornoAtual = aux_Retorno
        k += 1
    elif(len(bloqueado)>= 2):
            break
  return solucao_atual 

def perturbar_solucao(self, solucao_atual):
    selecionados = list()
    selecionados = solucao_atual 
    sorteiaClasse = random.randrange(0,3)
    for sorteiaClasse, teto in self.teto_de_gastos_por_classe.items():
        investimentos_dessa_classe = [investimento for investimento in self.investimentos if investimento.risco == sorteiaClasse]
        sorteiaInvestimento = random.randrange(0, len(investimentos_dessa_classe))
        if(investimentos_dessa_classe[sorteiaInvestimento] in selecionados and len([investimento for investimento in investimentos_dessa_classe if investimento in selecionados]) > self.min_investimentos_por_classe[sorteiaClasse]):
            del selecionados[sorteiaInvestimento]
        else:
          selecionados.append(investimentos_dessa_classe[sorteiaInvestimento])
          custo_total_ate_o_momento = sum(investimento.custo for investimento in selecionados)
          custo_dessa_classe = sum(investimento.custo for investimento in selecionados if (investimento.risco == sorteiaClasse and investimento in selecionados))
          if (custo_total_ate_o_momento > self.teto_orcamento or custo_dessa_classe > teto):
            del(selecionados[-1])
    return selecionados

def ILS(self,max_iter, kmax, solucao_inicial):
    melhor_solucao = solucao_inicial
    melhor_retorno = calc_retorno_esperado(self,melhor_solucao)
    for _ in range(max_iter):
        solucao_atual = perturbar_solucao(self, melhor_solucao)
        solucao_atual = RVND(self,kmax, solucao_atual)  # Aplica o VND para melhorar a solução perturbada
        retorno_atual = calc_retorno_esperado(self,solucao_atual)
        if retorno_atual < melhor_retorno:
            melhor_solucao = solucao_atual
            melhor_retorno = retorno_atual
    return melhor_solucao, melhor_retorno

class Otimizador:
  """
  Classe responsável pela otimização
  """
  def __init__(self, investimentos: list[Investimento],
               teto_de_gastos_por_classe: dict[Risco, float],
               min_investimentos_por_classe: dict[Risco, int],
               teto_orcamento: float):
    self.investimentos = investimentos
    self.teto_de_gastos_por_classe = teto_de_gastos_por_classe
    self.min_investimentos_por_classe = min_investimentos_por_classe
    self.teto_orcamento = teto_orcamento

  
  def construir_solucao_inicial(self)->list[Investimento]:
    """
    Constrói uma solução inicial factível,
    escolhendo os investimentos com menor custo possível
    respeitando o limite mínimo por classe
    Retorna lista com investimentos selecionados
    """

    selecionados = list()

    for classe, teto in self.teto_de_gastos_por_classe.items():
      min_investimentos = self.min_investimentos_por_classe[classe]
      investimentos_dessa_classe = [investimento for investimento in self.investimentos if investimento.risco == classe]
      investimentos_dessa_classe.sort(key = lambda x:x.custo)
      investimentos_selecionados = investimentos_dessa_classe[:min_investimentos]

      custo_dessa_classe = sum(investimento.custo for investimento in investimentos_selecionados)
      custo_total_ate_o_momento = sum(investimento.custo for investimento in selecionados)

      if custo_dessa_classe > teto:
        raise ValueError(f"Não existe solução factível. Custo mínimo da classe {classe} é R$ {custo_dessa_classe} que excede o teto de R$ {teto}")

      if custo_dessa_classe + custo_total_ate_o_momento > self.teto_orcamento:
        raise ValueError("Não existe solução factível. Impossível escolher o número mínimo de investimentos por classe sem exceder o teto orçamentário")

      selecionados += investimentos_selecionados
    
    return selecionados

  def otimimizar(self, numero_de_interacoes:int=100):
    inicio = time.time()
    solucao_atual = self.construir_solucao_inicial()
    '''
    print("solução inicial:")
    for investimento in solucao_atual:
      print(f'\t{investimento}')
    print(f"O custo total é R$ {sum(investimento.custo for investimento in solucao_atual)}")
    print(f"O retorno esperado total é R$ {sum(investimento.retorno for investimento in solucao_atual)}\n\n")
    '''
    ILS(self,50,50,solucao_atual)
    fim = time.time()
    print("Tempo de execução:",fim - inicio, )
    return solucao_atual

otimizador = Otimizador(investimentos,
                        teto_de_gastos_por_classe,
                        min_investimentos_por_classe,
                        teto_orcamento)

selecionados = otimizador.otimimizar()


print("Os investimentos selecionados aplicando ILS foram:")
for investimento in selecionados:
  print(f'\t{investimento}')

print(f"O custo total é R$ {sum(investimento.custo for investimento in selecionados)}")
print(f"O retorno esperado total é R$ {sum(investimento.retorno for investimento in selecionados)}")

    