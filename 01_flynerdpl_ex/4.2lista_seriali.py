# -*- coding: utf8 -*-
"""
Utwórz spis oglądanych seriali.
Każdy serial powinen mieć przypisaną ocenę w skali od 1-10.
Zapytaj użytkownika jaki serial chce obejrzeć. W odpowiedzi podaj jego ocenę.
Zapytaj użytkownika o dodanie kolejnego serialu i jego oceny.
Dodaj do swojego spisu.
"""

spis = {'House':9,'GoT':7,'Mentalista':6,'Sherlock':9}
print('''Czesc
      Ktory z tych seriali chcialbys obejrzec? powiemy Ci jak go oceniamy:''')
print(list(spis.keys())) #propozycja z komentarzy: UserSerial=input(„Podaj nazwę serialu jaki chcesz obejrzeć {}:”.format(list(Serials.keys())))
a=input()
print ('Nasza ocena tego serialu to:',spis[a])
print('Aby pomoc nam rozwijac baze seriali, dodaj prosze tytul serialu:')
b=input()
c=input('Oraz jego ocene:')
spis[b]=c
print('Aktualna lista seriali w bazie:\n',list(spis.keys()),'\nDziekuje za pomoc!')#nie wiem jak zapamietac wynik i rozszerzac liste co sesje

