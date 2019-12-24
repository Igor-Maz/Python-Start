# -*- coding: utf8 -*-
"""
Napisz skrypt obliczający wartość silnii.
Rozwiąż zadanie za pomocą pętli while(v1) oraz pętli for(v2).
"""

print('Policzymy sobie silnie\n')
a = int(input('Podaj jakąś liczbe: '))
count = 1
silnia=1
while count != a:
    count = count + 1
    silnia = silnia*count    
    #print(silnia, 'i', count)
print('silnia z liczby',a,'wynosi:',silnia)
silnia=str(silnia)
print('silnia z liczby',a,'zawiera',len(silnia),'cyfr')
