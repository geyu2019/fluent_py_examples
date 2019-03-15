import random

class BingoCage:
    def __init__(self,items):
        self._items = list(items)
        #random.shuffle(self._items)
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('PICK FROM EMPTY BINGOCAGE')
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))



print(bingo._items)
print(bingo.pick())
print(bingo())
print(bingo())

print(dir(bingo))
def test():
    return 0
print(dir(test))