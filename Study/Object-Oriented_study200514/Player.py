#coding utf-8

from itemlist import Potion

item1 = Potion()
item1.checkAmount()
print('Effect : %d' % (item1.using(3)))
item1.checkAmount()

# Source.
# https://wikidocs.net/16073
# https://wikidocs.net/63