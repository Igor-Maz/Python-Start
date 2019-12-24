# -*- coding: utf8 -*-
"""
Pobierz od użytkownika imię, nazwisko i numer telefonu,
a następnie:
    * Sprawdź czy imię i nazwisko składają się tylko z liter, a nr tel składa się wyłącznie z cyfr (wyświetl tę informację jako true/false)
    * Imię nazwisko popraw na pisane z dużej litery
    * Niektórzy podają numer telefonu z myślnikami lub z spacjami, usuń zbędne znaki z numeru
    * Sprawdź czy użytkownik jest kobietą
    * Połącz dane w jeden ciąg za pomocą spacji
    * Policz liczbę wszystkich znaków ww napisie
    * Podaj liczbę tylko liter w napisie
"""

print('czesc')
a=input('jak masz na imie?\n')
b=input('a jak na nazwisko?\n')
print('czy imie wprowadzono poprawnie?\n',a.isalpha())
print('czy nazwisko wprowadzono poprawnie?\n',b.isalpha())
c=a+' '+b
print('Witaj', c.title(),'\nPodaj prosze swoj numer telefonu:')
d=input()
d=d.replace(' ','').replace('-','')
print('czy numer wprowadzono poprawnie?\n',d.isdigit())
e=c.title()+' '+d.replace(' ','')
print('sprawdzam czy jestes kobieta:')
print(a.endswith('a'))
print(e)
print('rekord ma',len(e),'znakow')
print('Twoje Imie i Nazwisko ma',len(c)-1,'znakow')

