import math

def quadratic(a, b, c):
    # check the validity of arguements
    for e in (a, b, c):
        if not isinstance(e, (float, int)):
            raise TypeError('use integer or float as arguements')
    delta = b**2 - 4*a*c
    if delta < 0:
        print('no solution')
        return None
    elif delta == 0:
        return -b/(2*a)
    else:
        return (-b-math.sqrt(delta))/(2*a), (-b+math.sqrt(delta))/(2*a)

a = int(input('input a:'))
b = int(input('输入b'))
c = int(input('输入c'))
print(quadratic(a,b,c))
  

