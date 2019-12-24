# -*- coding: utf8 -*-
"""
A.Utwórz nowy plik, który po podaniu przez użytkownika
długości w cm będzie wyświetlał wynik w metrach i calach
zaokrąglając do x miejsc po przecinku.
"""

a=int(input('Czesc!\nPodaj dlugosc w cm:\n'))
b=a*0.394
c=a*0.01
print('{} centymetrow to {:.1f} metra albo {:.2f} cali'.format(a,c,b))
