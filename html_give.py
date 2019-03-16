
def cr (name,*content,cls=None,**attr):
    if cls is not None:
        clas=cls
    if attr:
        attr_str = "class=%s" % clas+''.join([" %s=%s" % (key, value ) for key,value in attr.items()])
    else:
        attr_str = ''

    if content :
        return ''.join("<%s %s> %s <%s>" %(name,attr_str,c,name) for c in content)

    else:
        return "<%s %s />" % (name,attr_str)

#print(cr("p"))
#print(cr("p","hi",cls="abb", src =1, href=1123))
#print(cr('p', 'hello'))
#print(cr("p",'hello','world'))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(cr(**my_tag))#Prefixing the my_tag dict with ** passes all its items as separate arguments,
                    # which are then bound to the named parameters, with the remaining caught by **attrs.

#print(cr.__code__.co_argcount)
#print(cr.__code__.co_varnames)
#print(cr.__code__.co_varnames[:cr.__code__.co_argcount])
from inspect import signature
sig = signature(cr)
#print(sig)
