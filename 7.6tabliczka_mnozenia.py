# -*- coding: utf8 -*-
"""
Wyświetl w konsoli klasyczną tabliczkę mnożenia. 
"""

szer = 14
print("-"*14)
print('| a | b |wyn.|')
print('*'*14)
for i in range(1,10):
    print(str(i)*14)
    for j in range(1,10):
        print('|{:3.0f}|{:3.0f}|{:4.0f}|'.format(i,j,i*j))
print('*'*14)        
