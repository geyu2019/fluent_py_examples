def fun(a,*list,b="B",c="C",**dict):
    print(a)
    print(list)
    print(b)
    print(c)
    print(dict)
    return 1
m={'name':'img', 'title':'Sunset Boulevard', 'src':'sunset.jpg', 'cls':'framed'}
list=[1,2,3,4,5,6,7,]
fun('aa',*list,**m)
print("================================")
fun('a',1,2,3,4,5,6,7,8,9,name=2,i=3,p=4)