
# methodcaller
from operator import methodcaller
s = 'The time has come'
print(s.upper())
upcase = methodcaller('upper')
print(upcase(s))
#simple implament
def methodcaller_t(str1):
    def f(obj):
        for i in dir(obj):
            if str1 == str(i):
                print(str1)
                print(str(i))
                return eval("obj.%s()" % str(i))
    return f
upcase_t = methodcaller_t('upper')
print(upcase_t(s))

