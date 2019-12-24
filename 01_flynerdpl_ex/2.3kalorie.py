# -*- coding: utf8 -*-
"""
kalkulator zapotrzebowania kalorycznego 2
Zapisz kalkulator BMR, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""

print('\nCzesc!')
a=input('Jak masz na imie?\n')
print('Milo Cie poznac',a.capitalize())
b=int(input('Ile masz lat?\n'))
c=int(input('Zeby poznac swoje zapotrzebowanie kaloryczne powiedz prosze ile wazysz:\n'))
d=int(input('Dzieki. A ile masz wzrostu (cm)?\n'))
BMI=c/((d/100)**2)
print('Twoje BMI wynosi: {:.1f}'.format(BMI))
e=10*c+6.25*d-5*b+5 #Kalkulator dla mezczyzny, dla kobiety byloby -161
print()
S=float(input('Podaj prosze swoj wspolczynnik aktywnosci, gdzie:\nPraca siedząca, brak dodatkowej aktywności fizycznej - 1.2\nPraca niefizyczna, mało aktywny tryb życia - 1.4\nLekka praca fizyczna, regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu - 1.6\nPraca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu - 1.8\nPraca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu - 2.0\n'))
print('\tDzieki',a.capitalize()+'!\n Twoje pelne zapotrzebowanie kaloryczne wynosi:\n\t {:.2f}'.format(e*S))
