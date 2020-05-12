import statistics
from math import sqrt

print(sqrt(x))

number_list = []

while True:
    number = input("Digite um número: ")
    if number.lower() == "f": break

    try:
        number = float(number) # Converte para float
        number_list.append(number)
    except:
        print("Você deve digitar um valor numérico.")


rol = sorted(number_list)

print(          '*' * 80)

print(f'''
      - Lista gerada em rol = {rol}\n
      - A média aritmética é igual a = {statistics.mean(number_list)}\n
      - O valor da média geometrica é =  {statistics.geometric_mean(number_list)}\n
      - O valor da media quadratica é = {sqrt(sum(number_list))/len(number_list)}\n
      - O valor da média harmônica é =  {statistics.harmonic_mean(number_list)}\n 
      - O valor da mediana é  =  {statistics.median(number_list)}\n
      - O maior valor é =  {rol[-1]}\n
      - O menor valor é =  {rol[0]}\n
      - O intervalo medio é = \n
      - O valor da amplitude é = {number_list[-1] - number_list[0]}\n
      - O valor do 50º percentil é =  {statistics.median_grouped(number_list)}\n
      - O valor da moda é =  {statistics.mode(number_list)}\n
      - Lista de modas (mais se repetem) = {statistics.multimode(number_list)}\n
      - Os valores dos quartis são =  {statistics.quantiles(number_list)}\n
      - O valor do desvio padrão é = ?????\n
      - O valor da variancia é= ???? \n
      - O valor da amplitude interquartil é = {statistics.quantiles(number_list)[-1] - statistics.quantiles(number_list)[0] }\n ''')

print(          '*' * 80)


