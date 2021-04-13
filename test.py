from ctypes import *

def test(x, y):
    x.append(1)
    y.append(2)
    print("diaoyong")

x,y = [], []
test(x,y)
print('x:',x,' y:', y)