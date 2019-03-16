from html_give import cr

print(cr)

from functools import partial

html = partial(cr,name = "p",cls = "ti")
#print(html)
print(html())
print(html(i='12')) #<p class=ti i=12 />
print("=============================")
#上面是官方库的运行情况，丢失了cls="ti",如果在html()中传入参数，这个问题就不会发生
#下面的实现也出现了同样的问题，为什么，还没有查出来
#simple implement
from inspect import signature

def partial1(f,*args,**kw):
    #print(args)
    #print(kw)
    print(f.__code__)
    print(f.__code__.co_varnames)
    print(f.__code__.co_argcount)
    sig = signature(f)
    print(sig.parameters)
    print("====================================")
    lis = []
    kwa = {}
    for i in args:
        lis.append(i)
    for key, value in kw.items():
        print(key)
        kwa[key] = value
    par=sig.bind(*lis,**kwa)
    par.apply_defaults()
    print(par.arguments)
    print('par.kwargs',par.kwargs)
    def temp (*a,**k):
        return f(*par.args,**par.kwargs)
    return temp

#html = partial1(cr,'p',"s", cls = "ti",cls1 = "ti",cls3 = "ti")
html = partial1(cr,name = "p",cls = "ti")
#print(html)
print(html(' '))

def partial2(f,*args,**kw):
    def temp (*a,**k):
        #print(k)
        #print(args)
        #print(a)
        lis=[]
        kwa={}
        for i in args:
            lis.append(i)
        #print(lis)
        t=["%s = %s" % (key,value)  for key , value in kw.items() ]
        for i in t:
            lis.append(i)
        #print(lis)
        tup = tuple(lis)
        return f(tup)
    return temp

html = partial2(cr,'s',name = "p",cls = "ti")
#print(html)
#print(html(n="11"))