# -*- coding:utf-8 -*-
class Student(object):
  def __init__(self,name,score):
    self.name=name
    self.score=score

class Animal(object):
  def run(self):
    print('Animal is running')

class Dog(Animal):
  def run(self):
    print('Dog is running...') 
 
class Cat(Animal):
  def run(self):
    print('Cat is runnng...')

dog=Dog()
dog.run()
cat=Cat()
cat.run()

def run_twice(animal):
  animal.run()
  animal.run()

run_twice(Animal())
run_twice(Dog())

class Timer(object):
  def run(self):
    print('Start...')

run_twice(Timer())
print('type()使用',type(123))
import types

def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
class MyObject(object):
  def __init__(self):
    self.x=9
  def power(self):
    return self.x*self.x

obj=MyObject()

print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
getattr(obj,'y')
getattr(obj,'z',404)

