def t(a=1):
    return 0;
print(t.__name__)

eval("print(t.__name__)")
for i in dir(t):
    if "name" in i:
        print(repr(i))
        eval("print(t.{})".format(str(i)))

class c:
    pass

print(dir(c))

print(sorted(set(dir(t))-set(dir(c))))

print(t.__annotations__)