# -*- coding: utf8 -*-
"""
Napisz skrypt, który, który obliczy stan konta za kilka lat.
Program pyta użytkownika o:
- stan początkowy konta,
- stopę oprocentowania rocznego
- liczbę lat na lokacie
Wynik wyświetl jako zdanie używając dowolnego sposobu formatowania tekstu.
Wypisz np. takie zdanie:
Twoje *stan_początkowy* zł przez *czas* lata na lokacie *oprocentowanie* % urośnie do *wynik*.
"""

print('Czesc.\nPoliczymy sobie dzisiaj ile zarobisz na koncie oszczednosciowym')
print()
a=float(input('ile srodkow przeznaczasz na lokate?\n'))
b=input('jakie oprocentowanie ma lokata nad ktora sie zastanawiasz?\n')
b=b.replace(',','.')
b=float(b)
p=(b/12)
n=int(input('na ile lat chcesz zalozyc lokate?\n'))
w=a*(1+p/100)**(n*12)
print('Po {} latach zgromadzisz na tym koncie {:.2f} zl'.format(n,w))
print('Twoj zysk to: {:.2f} zl'.format(w-a))
