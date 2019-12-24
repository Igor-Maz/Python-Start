# -*- coding: utf8 -*-
"""
Napisz prosty program, który wykona się zadaną przez użytkownika liczbę razy. Z każdym uruchomieniem pętli wyświetli informacje:
– czy liczba jest wielokrotnością 3
– czy liczba jest wielkorotnością 4
– wyświtli „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyświetli gwiazdkę, jeśli żaden z powyższych warunków nie jest spełniony
"""

a=int(input('ile liczb chcesz sprawdzic?'))
for x in range(a):
    b=int(input('podaj liczbe:'))
    if b%3==0 and b%4==0:
        print('hurra!',b,'jest podzielne zarowno przez 3 jak i 4')
    else:
        if b%3==0:
            print(b,'jest podzielne przez 3')
        elif b%4==0:
            print(b,'jest podzielne przez 4')
        elif b%3!=0 and b%4!=0:
            print('*',b,'nie jest podzielne ani przez 3 ani 4')
