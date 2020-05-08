# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:28:19 2020

I know it's complicated and can be done better, but I believe I found the result, not always the quick way is the right one, but I will try to learn.
@author: Vinicius
"""
   
'''    
def rain(item):
  
        if item % 3 == 0 and item % 5 == 0 and item % 7 == 0:
            print("PlingPlangPlong")
        elif item % 3 == 0 and item % 5 == 0:
            print('PlingPlang')

        elif item % 3 == 0 and  item % 7 == 0: 
            print('PlingPlong')
        elif item % 5 == 0 and item % 7 == 0:   
            print("PlangPlong")
        elif item % 3 == 0:
            print("Pling")
        elif item % 5 == 0:
            print("Plang")
        elif item % 7 == 0:
            print("Plong")
        else:
            print(item)
        
    
rain(15)        
  '''          
def convert(number):
    result = ""
    if number%3 == 0:
        result += "Pling"
    if number%5 == 0:
        result += "Plang"
    if number%7 == 0:
        result += "Plong"
    if result == "":
        result = str(number)

    return result   

convert(10)
    