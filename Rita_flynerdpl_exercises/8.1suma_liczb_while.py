# -*- coding: utf8 -*-
"""
Napisz program z wykorzystaniem pętli while,
który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik dla liczby "1": 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
"""

a = int(input('podaj dowolna liczbe: '))
count = 1
suma = a
while count != 10:
    a = a+ 1;
    suma=suma+a
    count= count + 1;
    #print(count , 'i', a,'i',suma)
print('suma 10 kolejnych liczb to:',suma)
