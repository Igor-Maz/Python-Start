# -*- coding: utf8 -*-
"""
Do kalkulatora BMI z lekcji "Python 1 zabawy w konsoli"
dodaj sprawdzanie czy BMI jest prawidłowe

Niedowaga       |   < 18,5
Waga normaln    |   18,5 – 24
Lekka nadwaga	|   24 – 26,5
Nadwaga	        |   > 26,5

W przypadku nadwagi sprawdź czy występuje otyłość:

Otyłość I stopnia   |	30 – 35
Otyłość II stopnia  |	30 – 40
Otyłość III stopnia |	> 40
"""

print('Czesc!')
a=float(input('\nPodaj wage w kg\n'))
b=float(input('Podaj wzrost w cm\n'))
bmi=(a/(b/100)**2)
print('\nTwoje BMI wynosi: {:.1f}'.format(bmi),'i jest to ',end='')
if bmi<=18.5:
    print('niedowaga (ponizej 28,5)')
elif bmi<=24:
    print('normalna waga (18,5 - 24)')
elif bmi<=26.5:
    print('lekka nadwaga (24 - 26.5)')
elif bmi>26.5:
    print('problem :/\n'+'...')
    if 26.5<bmi<30:
        print('ale nie wielki - Nadwaga (26.5 - 30)')
    elif 30<=bmi<35:
        print('warto by sie za siebie wziac - Otylosc I stopnia (30 - 35)')
    elif 35<=bmi<40:
        print('trzeba sie za siebie wziac - Otylosc II stopnia (35 - 40)')
    else:
        print('jest niebezpiecznie - Otylosc III stopnia (40+)')
print('Dzieki i powodzenie!')
