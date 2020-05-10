# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:54:19 2020

@author: Vinicius
"""

#def operation(soma,sub,div,mult)
#Caculadora.py

#1 imprimir na tela python calculator
#2 imprimir na tela uma mensagem desejando o usuario a escolhar uma opção
#3 imprimir na tela as mensagem de 1 a 4
#4 pedir ao usuario para digitar a senha
#5 digite 2 numeros
#6 opção invalida se nao escolheu uma das 4 opções

import math

option = int(input('Digite a opção desejada:'))
x = int(input("digite o primeiro numero:"))
y = int(input("digite o segundo numero:"))

print('*'*10 + ' Python Calculadora ' + '*'*10 )

print()
#opção 1 = soma de x e y
#opção 2 = subtração x e y
#opçao 3 = divisao x e y
#opçao 4 = multiplicacao x e y        
#z = int(input('digite novamente a operação desejada:'))    
if option == 1:
    print(f'     O resultado da soma é:  {x+y}')
elif option == 2:
    print(f'     O resultado da subtração é: {x-y}')
elif option == 3:
    print(f'     O resultado da divisão é: {x/y}')
elif option == 4:
    print(f'     O resultado da multiplação é: {x*y}')
else: 
    print("Operação matematica não foi definida")

print()
 
      
print('*'*40 )        
        
        
        
        
        
        