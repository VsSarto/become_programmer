from ast import literal_eval;  # Para avaliar o literal
from re import compile;  # Para compilar a expressão regular
import statistics

number_list = []  # Lista de resultados

# Fonte: https://stackoverflow.com/a/385597/11379709
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

    class StatisticsError(ValueError):
        pass

    def __init__(self,values):
        self.values = values

    def rol(self):    
        print(f'Lista gerada em rol = {sorted(self.values)}\n')

    def media(self):
        print(f'O valor da média aritmética é = {statistics.mean(self.values)}\n')

    def media_geo(self):
        try:
            print(f'O valor da média geometrica é = {statistics.geometric_mean(self.values)}\n')

        except:
            print('O valor da média geometrica é = A média geometrica requer numeros positos diferentes de zero, operação inválida.\n')

    def media_har(self):
        try:
            print(f'O valor da média harmônica é = {statistics.harmonic_mean(self.values)}\n')
        except:
            print(f'O valor da média harmônica é = Operação inválida para numeros negativos e nulos.\n')

    def mediana(self):
        print(f'O valor da mediana é  =  {statistics.median(self.values)}\n')

    def menor(self):
        print(f'O menor valor é =  {sorted(self.values)[0]}\n')

    def maior(self):
        print(f'O maior valor é =  {sorted(self.values)[-1]}\n')

    def amplitude(self):
        print(f'O valor da amplitude é = {self.values[-1] - self.values[0]}\n')

    def inter_m(self):
        print('O intervalo medio é =\n ')

    def percentil(self):
        print(f'O valor do 50th percentil é =  {statistics.median_grouped(self.values)}\n')

    def moda(self):
        print(f'O valor da moda é =  {statistics.mode(self.values)}\n')

    def modas(self):
        print(f'Lista de modas (mais se repetem) = {statistics.multimode(self.values)}\n')

    def quartis(self):
        print(f'Os valores dos quartis são =  {statistics.quantiles(self.values)}\n')

    def a_interquartil(self):
        print(f'O valor da amplitude interquartil é = {statistics.quantiles(self.values)[-1]-statistics.quantiles(self.values)[0]}\n')

    def devpadrao(self):
        print(f'O valor do desvio padrão amostral é = {statistics.stdev(self.values)}\n')

    def varian(self):
        print(f'O valor da variância amostral é = {statistics.variance(self.values)}\n')

    def devpadrao_p(self):
        print(f'O valor do desvio padrão populacional é = {statistics.pstdev(self.values)}\n')

    def varian_p(self):
        print(f'O valor da variância populacional é = {statistics.pvariance(self.values)}\n')



print('_'*75)
operation_1 = Metode(number_list)
operation_1.rol()

operation_2 = Metode(number_list)
operation_2.media()

operation_3 = Metode(number_list)
operation_3.media_geo()

operation_4 = Metode(number_list)
operation_4.media_har()

operation_5 = Metode(number_list)
operation_5.mediana()

operation_6 = Metode(number_list)
operation_6.menor()

operation_7 = Metode(number_list)
operation_7.maior()

operation_8 = Metode(number_list)
operation_8.amplitude()

operation_9 = Metode(number_list)
operation_9.inter_m()

operation_10 = Metode(number_list)
operation_10.percentil()

operation_11 = Metode(number_list)
operation_11.moda()

operation_12 = Metode(number_list)
operation_12.modas()

operation_13 = Metode(number_list)
operation_13.quartis()

operation_14 = Metode(number_list)
operation_14.a_interquartil()

operation_15= Metode(number_list)
operation_15.devpadrao()

operation_16 = Metode(number_list)
operation_16.varian()

operation_17= Metode(number_list)
operation_17.devpadrao_p()

operation_18 = Metode(number_list)
operation_18.varian_p()


print('_'*75)


