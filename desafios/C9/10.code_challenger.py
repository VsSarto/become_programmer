# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:37 2020

@author: Vinicius
"""




first_name = input('whats is your first name?')
last_name = input('whats is your first name?')

l_first = first_name[0]
l_last = last_name[0]



if len(first_name) < 10 and len(last_name) < 10:
    print(first_name.title() + '' + last_name.title())

elif len(first_name) >= 10 and len(last_name) < 10:
    print(l_first +'.' + ' ' + last_name)
    
elif len(first_name) < 10 and len(last_name) >= 10:
    print(first_name + ' ' + l_last)
elif len(first_name) >=10 and len(last_name) >= 10:
    print(last_name)
       

