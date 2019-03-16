from functools import reduce
from operator import add
#reduce
a = [1,11,111,1111,111111,1111111]
print(reduce(add,a))
print(reduce(add,range(1000)))

print(sum(a))

#print(reduce(lambda x,y: , a))
print("=========")
def fact(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
print(fact(15000))
def fact_test(n):   #逻辑混乱，不足取，test2的逻辑至少清晰
    def f(a,b):
        return a*b

    def reduce_1(f,list,n=0,sum=1):
        #print(n)
        if n==0 :
            sum = list[0]
            return reduce_1(f, list, n + 1, sum)
        if n == len(list):
            return f(n,sum)

        if (n>0 and n<(len(list)-1)) :
            #print(list[n])
            a=f(list[n],sum)
            sum =a
            #print(sum)
            return reduce_1(f,list,n+1,sum)
    list=range(1,n+1)
    return(reduce_1(f,list))
print(fact_test(10))
def fact_test2(n):
    def f(a,b):
        return a*b

    def reduce_2(f,list,n=0,sum=1):
        #print(n)
        if n==0 :
            sum = list[n]
            return reduce_2(f, list, n + 1, sum)
        else:
            if n == len(list)-1:
                return f(list[n],sum)

            else:
                if (n>0 and n<(len(list))) :
                    a=f(list[n],sum)
                    sum =a
                    return reduce_2(f,list,n+1,sum)
    list=range(1,n+1)
    return(reduce_2(f,list))
print(fact_test2(10))

def fact_test_liter(n):
    def f(a,b):
        return a*b
    def reduce_3(f,list,count=0):
        if count == n-1:
            return list[count]
        else:
            print(count)
            return f(list[count],reduce_3(f,list,count+1))
    return reduce_3(f,range(1,n+1))
print(fact_test_liter(10))

def reduce_liter(f,list,count=0):
    if count == len(list)-1:
        return list[count]
    else:
        return f(list[count],reduce_liter(f,list,count+1))
print("===================")
print(reduce_liter(lambda x,y: x*y , range(1,999)))
def reduce_iter(f,list,n=0,sum=1):
        #print(n)
        if n==0 :
            sum = list[n]
            return reduce_iter(f, list, n + 1, sum)
        else:
            if n == len(list)-1:
                return f(list[n],sum)

            else:
                if (n>0 and n<(len(list))) :
                    a=f(list[n],sum)
                    sum =a
                    return reduce_iter(f,list,n+1,sum)
print("===================")
print(reduce_iter(lambda x,y: x*y , range(1,999)))


#map
#map的第一个参数是函数，此函数只接受一个参数
print('\nmap+++++++++++++++++++++++++++++++++++++++map\n')
from operator import mul
from functools import partial
triple = partial(mul, 3)
a=list(map(triple, range(1, 10)))
print(a)
#filter