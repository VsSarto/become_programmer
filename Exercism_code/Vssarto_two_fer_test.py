# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:29:50 2020

@author: Vinicius
"""


x = input('enter a name:')
if x == '':
        try:
            raise NameError('one for you, one for me.')
        except NameError:
            raise
else:
    
    print(f' One for {x}, one for me.')
        
        
        
        
        