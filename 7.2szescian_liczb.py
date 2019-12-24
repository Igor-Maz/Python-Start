# -*- coding: utf8 -*-
"""
Napisz program, który dla 10 kolejnych liczb naturalnych
wyświetli ich ich wartość do sześcianu.
"""

print('szescian pierwszych 10 liczb naturalnych:')
for i in range(1,11):
    print(i*i*i)
print('szescian dowolnych kolejnych liczb naturalnych:')
b=int(input('podaj pierwsza z nich:'))
for j in range(b,b+10):
    print(j*j*j)
    
