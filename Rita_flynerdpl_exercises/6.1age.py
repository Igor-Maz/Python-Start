# -*- coding: utf8 -*-
"""
Zapytaj użytkownika o wiek.
W zależności od wieku zwróć czy użytkownik jest już pełnoletni
lub ile lat zostało mu do pełnoletności,
Użytkownikom powyżej 100lat życz 200 ;)
"""

age = int(input('ile masz lat?\n'))

if age > 100:
    print('serio? 200 lat, juz nic Ci nie zaszkodzi')
    quit()
else:
    respon = input('mozna Ci ufac? T/N\n')
respon=respon.upper()

if age >= 18 and respon == 'T':
    print('bravo, mozesz pic juz od:', age-18 , 'lat')
elif respon != 'T':
    print('lepiej nie pij')
else:
    print('zostalo Ci jeszcze:' , 18-age)
