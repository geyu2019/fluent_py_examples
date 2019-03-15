import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._ranks = [rank for rank in self.ranks]
        self._cards = [Card(rank, suit) for suit in self.suits \
                                       for rank in self.ranks]

    def __len__(self):
        print('调用了len，但是我胡乱输出')
        return 10
        #return len(self._cards)

    def __getitem__(self,position):
        #return self._cards[position]
        return self._ranks[position]
poke = FrenchDeck()

print(poke.__len__())
print(poke.__getitem__(10))
print(len(poke))

from random import choice

print(choice(poke))

print(poke[2])
print(Card('Q', 'hearts') in poke)
print(poke.ranks)
print(poke._ranks)
print('A' in poke)
for i in poke:
    print(i)
