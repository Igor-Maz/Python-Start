# -*- coding: utf8 -*-
"""
Utwórz listę imion męskich / żeńskich.
Użytkownik podaje imię.
Jeśli imię istnieje na liście wyświetl czy jest to imię męskie czy żeńskie
Jeżeli nie dodaj imię do zbioru wraz z oznaczeniem płci.
"""

kobiece = ['Marta','Ula','Arletta','Maria','Natalia','Marzena','Sylwia','Teresa','Dorota']
meskie = ['Igor','Bartek','Darek','Andrzej','Slawek','Jacek','Lukasz','Tomasz','Piortek','Piotr']
a=input('Podaj imie do sprawdzenia:')
a=a.capitalize()
if a in kobiece:
    print('to imie jest kobiece')
elif a in meskie:
    print('to imie jest meskie')
else:
    b=input('nie znamy tego imienia, podaj prosze plec K/M:')
    b=b.lower()
    if b=='k':
        kobiece.append(a) #funkcja z googla
        print(kobiece)
    else:
        meskie.append(a)
        print(meskie)
        
