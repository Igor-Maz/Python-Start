# -*- coding: utf8 -*-
"""
Napisz program,
który dla 10 kolejnych liczb naturalnych
wyświetli sumę poprzedników.
"""

print('suma pierwszych 10 liczb naturalnych:')
a=0
for i in range(1,11):
    a=a+i
    print(a)
print('suma dowolnych kolejnych liczb naturalnych:')
b=int(input('podaj pierwsza z nich:'))
print(b)
for j in range(b+1,b+10):
    b=b+j
    print(b)
