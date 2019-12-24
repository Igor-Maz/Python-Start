# -*- coding: utf8 -*-
"""
Spróbuj wyświetlić choinkę z trójkątów w taki sposób,
aby każdy poziom choinki był o 1 wiersz dłuższy:

#
##
#
##
###
#
##
###
####
"""

a=int(input('jak duza ma byc choinka?'))

for i in range(a):
    for j in range(i+2):
        for k in range(j+1):
            print('#', end='')
        print()
#tego zadania nie kumam
