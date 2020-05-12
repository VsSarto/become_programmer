import statistics
from math import sqrt
from re import compile;  # Para compilar a expressão regular
from ast import literal_eval;  # Para avaliar o literal

# Escolhendo função 

choice = [] 

# Fonte: https://stackoverflow.com/a/385597/11379709
# Atribuindo os valores da lista

number_list = []  # Lista de resultados

re_float = compile("""(?x)
   ^
      [+-]?\s*      #  Que inicialmente, corresponda a um sinal opcional seguido ou não de espaço(s)
      (             
          \d+       # Ou corresponde a um ou mais digitos...
          (\.\d*)?  # ...seguido(s) ou não de um ponto e zero ou mais digitos
         |\.\d+     # Ou um ponto seguido de dígitos
      )
      ([eE][+-]?\d+)?  # Podendo ou não ter a notação exponencial
   $""")

while True:
    print("Digite um número ou f para sair:")
    entrada = input()
    if entrada.upper() == 'F': break;  # Se a entrada for f ou F abandona o laço
    entrada = re_float.fullmatch(entrada)  # Tenta validar a entrada como numérico
    if entrada:
        # Se houver exito na validação
        number_list.append(literal_eval(entrada.group(0)))  # Adiciona o valor literal da entrada na lista de resultados
    else:
        # Caso não haja exito na validação
        print("Entrada inválida...")


class Metode:

    def __init__(self,values):
        self.values = values
        

    def media(self):
        return statistics.mean(self.values)

    def media_geo(self):
        return statistics.geometric_mean(self.values)

    def media_har(self):
        return statistics.harmonic_mean(self.values)

    def mediana(self):
        return statistics.median(self.values)


    def menor(self):
        return sorted(self.values)[0]

    def maior(self):
        return sorted(self.values)[-1]

    def amplitude(self):
        return sorted(self.values)[-1] -sorted(self.values)[0]

    def inter_m(self):
        return 

    def percentil(self):
        return statistics.median_grouped(self.values)

    def moda(self):
        return statistics.mode(self.values)

    def modas(self):
        return statistics.multimode(self.values)    

    def quartis(self):
        return statistics.quantiles(self.values)

    def devpadrao(self):
        return 

    def a_interquartil(self):
        return     
        


#lista em rol
rol = sorted(number_list)

#enumerando as operacoes
operation_0 = Metode(number_list)
operation_1 = Metode(number_list)
operation_2 = Metode(number_list)
operation_3 = Metode(number_list)
operation_4 = Metode(number_list)
operation_5 = Metode(number_list)
operation_6 = Metode(number_list)
operation_7 = Metode(number_list)
operation_8 = Metode(number_list)
operation_9 = Metode(number_list)
operation_10 = Metode(number_list)
operation_11 = Metode(number_list)
operation_12 = Metode(number_list)
operation_13 = Metode(number_list)
operation_14 = Metode(number_list)
operation_15 = Metode(number_list)
operation_16 = Metode(number_list)
operation_17 = Metode(number_list)
operation_18 = Metode(number_list)

#operation_0 = resulta em todas as operações


#operation_1 = Média aritmética.
print((operation_1.media())

#operation_2  = Média geométrica de dados.
operation_2.media_geo()

#operation_3  = Média harmônica dos dados.
operation_3.media_har()

#operation_4  = Mediana (valor médio) dos dados.  
operation_4.mediana()

#operation_5  = Menor valor dos dados.
operation_5.menor()

#operation_6  = Maior valor dos dados.
operation_6.maior()

#operation_7  = Maior valor menos o menor valor.
operation_7.amplitude()

#operation_8  = Intervalo medio entre os dados.
operation_8.inter_m()

#operation_9  = Mediana, ou percentil 50, de dados agrupados.
operation_9.percentil()

#operation_10 =	Moda dos dados.
operation_10.moda()

#operation_11 = Lista da moda (valores mais comuns dos dados).
operation_11.modas()

#operation_12 = Divide os dados em intervalos com igual probabilidade.
operation_12.quartis()

#operation_13  = desvio padrão, medida de dispersão em torno da média.
operation_13.devpadrao()

#operation_14  = Amplitude interquartil, grau de espalhamento de dados em torno da medida de centralidade.
operation_14.a_interquartil()