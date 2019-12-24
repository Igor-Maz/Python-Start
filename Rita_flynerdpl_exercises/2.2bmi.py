# -*- coding: utf8 -*-
"""
kalkulator BMI 2
Zapisz kalkulator BMI, który wcześniej był w konsoli do pliku,
tak aby pytał użytkownika o potrzebne do obliczeń dane.
"""

print('Czesc!')
a=float(input('\nPodaj wage w kg\n'))
b=float(input('Podaj wzrost w cm\n'))
print('\nTwoje BMI wynosi: {:.0f}'.format(a/(b/100)**2))
