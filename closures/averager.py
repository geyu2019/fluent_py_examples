class Averager():

    def __init__(self):
        self.series = []
    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
ave = Averager()
print(ave(10))
print(ave(11))
print(ave(12))

def aver():
    dict={'total':0,'time':0}
    def ave(value):
        dict['total'] +=value
        dict['time'] += 1
        return dict['total']/dict['time']
    return ave
ave_fun = aver()
print(ave_fun(10))
print(ave_fun(11))
print(ave_fun(12))
print(ave_fun.__code__.co_varnames)
print(ave_fun.__code__.co_freevars)
print(ave_fun.__closure__)
#print(ave_fun.__closrue__.cell_content)
print("-==============================--------------------------------")


def aver():
    total = 0
    time  = 0
    def ave(value):
        nonlocal total,time
        total +=value
        time  +=1
        return total/time
    return ave
ave_fun = aver()
print(ave_fun(10))
print(ave_fun(11))
print(ave_fun(12))
print(ave_fun.__code__.co_varnames)
print(ave_fun.__code__.co_freevars)
print(ave_fun.__closure__)
#print(ave_fun.__closrue__.cell_content)
