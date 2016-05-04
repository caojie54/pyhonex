# -*- coding:utf-8 -*-
L1=['hello','world',18,'Apple',None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)
for s in L2:
	print(s)

L3=[s.lower() if isinstance(s,str) else s for s in L1]
print(L3)
