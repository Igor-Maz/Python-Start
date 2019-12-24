# -*- coding: utf8 -*-
"""
Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
Następnie powitaj każdą osobę na liście.
"""

a=str(input('wpisz dowolna liczbe imion rozdzielajac je przecinkiem lub spacja:'))
a=a.replace(' ',',').title().split(sep=',')
for name in a:
    print('Czesc',name)
