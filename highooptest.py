# -*- coding:utf-8 -*-
class Student(object):
 pass

s=Student()
s.name='Michael'#dsfdsfs
print(s.name)

def set_age(self,age):
  self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

class Highstudent(object):
  __slots__=('name','age')

s=Highstudent()
s.name='Michael'
s.age=25
print(s.age)

class Screen(object):
  @property
  def width(self):
    return self._width
   
  @width.setter
  def width(self,value):
    if not isinstance(value,int):
      raise ValueError('width must be an integer!')
    self._width=value

  @property
  def height(self):
    return self._height

  @height.setter
  def height(self,value):
    if not isinstance(value,int):
      raise ValueError('height must be an integer!')
    self._height=value
  
  @property
  def resolution(self):
    return self._width*self._height
    
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
assert s.resolution==786432,'1024*768=%d?'% s.resolution
