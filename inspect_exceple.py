from inspect import signature
from html_give import cr
from inspect import signature
sig = signature(cr)
print("=====================================")
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',  'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
for name,value in bound_args.arguments.items():
    print(name,'=',value)

