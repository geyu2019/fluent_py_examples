
str = 'ctr葛1'
print(len(str))

strb = str.encode('utf-8')
print(strb)
print(len(strb))
[print(strb[i]) for i in range(len(strb))]
import array
numbers1 = array.array('b', [-2, -1, 0, 1, 2])#array
numbers2 = array.array('h', [-2, -1, 0, 1, 2])
#numbers = [-2, -1, 0, 1, 2,'a']
octets1 = bytes(numbers1)
print(octets1)
print(len(octets1))
octets2 = bytes(numbers2)
print(octets2)
print(len(octets2))
