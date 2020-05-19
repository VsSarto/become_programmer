from ast import literal_eval;  # Para avaliar o literal
from re import compile;  # Para compilar a expressão regular
from pandas import Series
from pandas import DataFrame
import statistics
import numpy

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
    if entrada.upper() == 'F': break;
    entrada = re_float.fullmatch(entrada)
    if entrada:

        number_list.append(literal_eval(entrada.group(0)))
    else:

        print("Entrada inválida...")

frame = DataFrame((number_list), columns= ['Dados Coletados'])

print('-'* 40)
print(f' Os dados em rol: {sorted(number_list)}')

print('-'* 40)

print(frame.describe())

print('-'* 40)


