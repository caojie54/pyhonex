# -*- coding:utf-8 -*-
class Hello(object):
  def hello(self,name='world'):
    print('Hello,%s.'% name)
def fn(self,name='world'):
  print('hello,%s.'% name)

Hi=type('Hi',(object,),dict(hello=fn))
h=Hi()
h.hello()
print(type(Hi))
print(type(h))
