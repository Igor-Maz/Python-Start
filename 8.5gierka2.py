# -*- coding: utf8 -*-
"""
Korzystając z modułu random stwórz kolejną prostą grę.
Komputer losuje słowo z dostępnego zakresu (posiada listę słów).
Następnie litery są mieszane.
Wymieszane litery pokazywane są graczowi.
Gracz musi zgadnąć co to za słowo. Gracz zgaduje do skutku.
Dopiero zgadnięcie przerywa grę.

Rozszerzenie: gracz może wybrać na klawiaturze „q” lub „Q”,
aby zakończyć grę przed czasem.
"""

print('Hej! Pobawimy sie w gre :) \nZa chwile zobaczysz ciag liter. Uloz z nich wyraz. \nJezeli bedzie to wyraz z naszej listy - wygrales! Probuj do skutku. \nNacisnij "q" lub "Q" zeby zakonczyc gre. \nPowodzenia!')
import random
lista=['alert','bonifacy','celofan','diplodok','errata','fikusny','geralt',
       'hieronim','ignorant','jurny','kloaczny','ludzmirskie','milion','nikogo',
       'opactwo','przejebane','ruzga','slabeusz','tornister','zaklopotany']
a = random.choice(lista)
b=len(a)
c=random.sample(a,b)
print('Uloz slowo z podanych liter: ',c)
count=0
while 1:
    count=count+ 1
    shoot=input('Twoj strzal to: ')
    if shoot == a:
        print('Tak jest!')
        print('Wygrales, gratuluje!')
        break
    elif shoot == 'q' or shoot == 'Q':
        print('Wyszedles z gry')
        break
    else:
        print('Niestety, to nie jest to slowo')
        if count == 2:
            d=input('czy chcesz zobaczyc pierwsza litere? (t/n) ')
            if d=='t':
                print('Szukane slowo zaczyna sie na litere:', a[0])
        elif count == 5:
                d=input('To juz Twoja 5 proba, czy chcesz zobaczyc trzy pierwsze litery? (t/n) ')
                if d=='t':
                     print('Pierwsze trzy litery szukanego slowa to:', a[:3])
        elif count == 8 or count == 10 or count == 12 or count ==15:
                print('Pamietaj ze mozesz zaczac od poczatku z nowym slowem.')
                shoot=input('Wcisnij "q" zeby wyjsc, lub dowolny inny klawisz zeby kontynuowac: ')
                if shoot == 'q' or shoot == 'Q':
                    print('Wyszedles z gry')
                    break
                else:
                    continue


