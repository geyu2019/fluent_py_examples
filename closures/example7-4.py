b = 5
def f1(a):
    global b
    print(a)
    print(b)
    a=7
    print(a)
    b=0
f1(3)
print(b)
from dis import dis
dis(f1)