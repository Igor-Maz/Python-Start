# -*- coding: utf8 -*-
"""
Wskaż najwyższą wartość z 3 liczb
i posortuj je od największej do najmniejszej.
"""

a=int(input('wprowadz pierwsza liczbe: '))
b=int(input('wprowadz druga liczbe: '))
c=int(input('wprowadz trzecia liczbe: '))

if a==b or a==c or b==c :
    print('liczby sie dubluja')
    print('wiecej niz jedna liczba jest najwieksza')
    
if a>b and a>c :
    print('najwieksza z podanych liczb jest: ',a)
    d=a
    if b>c:
        e=b
        f=c
    else:
        e=c
        f=b
elif b>a and b>c :
    print('najwieksza z podanych liczb jest: ',b)
    d=b
    if a>c:
        e=a
        f=c
    else:
        e=c
        f=a
elif c>a and c>b :
    print('najwieksza z podanych liczb jest: ',c)
    d=c
    if a>b:
        e=a
        f=b
    else:
        e=b
        f=a
else:
    d=str('brak')
if d!='brak':
    print('liczby od najwiekszej do najmniejszej:\n',d,e,f)
    
#Sortowanie Rity przy zalozeniu ze nie ma dubli:
''' 
if x < y:
    temp = x
    x = y
    y = temp
if x < z:
    temp = x
    x = z
    z = temp
if y < z:
    temp = y
    y = z
    z =temp
print (x , y, z)
'''

#od innego uzytkownika:
'''
if (a<=b):
    if (c<=a):
        print(c, a, b)
    else:
        if (b<=c):
            print(a, b, c)
        else:
            print(a, c, b)
else:
    if(c<=b):
        print(c, b, a)
    else:
        if(c<=a):
            print(b,c,a)
        else:
           print(b,a,c)
'''




  
