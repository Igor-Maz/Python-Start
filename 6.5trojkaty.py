# -*- coding: utf8 -*-
"""
Na podstawie długości a,b,c - sprawdź
- czy są to ramiona trójkąta
- czy trójkąt jest pitagorejski
- czy jest to trójkąt egipski
Weź pod uwagę, że wartości mogą bbć zczbtbwane w dowolnej kolejności.
"""

a=int(input('dlugosc pierwszego boku "a": '))
b=int(input('dlugosc drugiego boku "b": '))
c=int(input('dlugosc trzeciego boku "c": '))

if a+b<=c or b+c<=a or a+c<=b:
    print('To nie jest trojkat Prosiaczku')
else:
    if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print('Ten trojkat jest pitagorejski ',end='')
        if (a%3==0 or a%4==0 or a%5==0) and (b%3==0 or b%4==0 or b%5==0) and (c%3==0 or c%4==0 or c%5==0):
            print('i w dodatku egipski')
    elif a**2+b**2<c**2 or a**2+c**2<b**2 or b**2+c**2<a**2:
        print('Ten trojkat jest rozwartokatny')
    elif a**2+b**2>c**2 or a**2+c**2>b**2 or b**2+c**2>a**2:
        print('Ten trojkat jest ostrokatny')
