import statistics
from math import sqrt
from re import compile;  # Para compilar a expressão regular
from ast import literal_eval;  # Para avaliar o literal

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


def todas(self):
    print(f'''
      {'*' * 50}\n
      - Lista gerada em rol = {sorted(number_list)}\n
      - A média aritmética é igual a = {statistics.mean(number_list)}\n
      - O valor da média geometrica é =  {statistics.geometric_mean(number_list)}  ??????\n
      - O valor da media quadratica é = {sqrt(sum(number_list)) / len(number_list)} ?????\n
      - O valor da média harmônica é =  {statistics.harmonic_mean(number_list)}\n 
      - O valor da mediana é  =  {statistics.median(number_list)}\n
      - O maior valor é =  {sorted(number_list)[-1]}\n
      - O menor valor é =  {sorted(number_list)[0]}\n
      - O intervalo medio é = \n
      - O valor da amplitude é = {number_list[-1] - number_list[0]}\n
      - O valor do 50º percentil é =  {statistics.median_grouped(number_list)}\n
      - O valor da moda é =  {statistics.mode(number_list)}\n
      - Lista de modas (mais se repetem) = {statistics.multimode(number_list)}\n
      - Os valores dos quartis são =  {statistics.quantiles(number_list)}\n
      - O valor do desvio padrão é = ?????\n
      - O valor da variancia é= ???? \n
      - O valor da amplitude interquartil é = {statistics.quantiles(number_list)[-1] - statistics.quantiles(number_list)[0]}\n
      {'*' * 50}''')


todas(number_list)


#REVISAR OS ITENS COM ??????????????