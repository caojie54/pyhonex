# -*- coding:utf-8 -*-
def by_name(t):
    s=t[0].lower()
    return s
L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
print('sorted by name')
L2=sorted(L,key=by_name)
print(L2)


def by_score(t):
    s=t[1]
    return s
print('sorted by score reverse')
L3=sorted(L,key=by_score,reverse=True)
print(L3)
print('sorted by score ')
L4=sorted(L,key=by_score)
print(L4)
