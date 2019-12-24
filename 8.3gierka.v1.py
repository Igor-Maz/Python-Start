# -*- coding: utf8 -*-
"""
Zapoznaj się z modułem random.
>>> import random
Stwórz prostą grę zgadywankę.
Komputer losuje wartość z przedziału od 1-30.
Poproś użytkownika o zgadnięcie liczby.
Program pyta użytkownika o podanie liczby tak długo,
dopóki gracz nie zgadnie.

Rozszerz grę z punktu powyżej.
Gracz powinen otrzymać informację czy jego liczba jest za duża czy za mała.
"""

import random
a = (random.randint(1,20))
print('Odgadnij jaka liczbe wylosowal komputer!')
b=int(input('podaj liczbe w zakresie 1-20: \n'))
while 1:
    if a == b:
        print('Brawo, zgadłeś')
        break
    elif a<b:
        print('podana liczba jest zbyt duza')
        print('probuj dalej')
        b=int(input('podaj liczbe w zakresie 1-20: \n'))
    elif a>b:
        print('podana liczba jest zbyt mala')
        print('probuj dalej')
        b=int(input('podaj liczbe w zakresie 1-20: \n'))
