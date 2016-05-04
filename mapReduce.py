# -*- coding:utf-8 -*-
from functools import reduce
def str2float(s):
    a=s.index('.')
    print(a)
    def fn1(x,y):
      return x*10+y
    return reduce(fn1,map(int,s[:a]))+reduce(fn1,map(int,s[a+1:]))/(10**len(s[a+1:]))
print('str2float=',str2float('123.456'))
