# -*- coding:utf-8 -*-
import functools
def log(text='call'):
 def decorator(func):
  @functools.wraps(func)
  def wrapper(*args,**kw):
    print('%s %s():'%(text,func.__name__))
    func(*args,**kw)
    print('%s end:'% text)
  return wrapper
 return decorator

#@log('hastext')
@log()
def now():
  print('2015-3-25')

now()
