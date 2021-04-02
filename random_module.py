#generating a rendom number between 0 and one
import random

a = random.random()
# print(a)

#random number between any two integer
b = random.randint(2,5)
# print(b)

#random nubmer in a given range
c = random.randrange(1,10)
# print(c)

# random choice from a list
list_ =  ['blue', 'red','green']
d = random.choice(list_)
# print(d)

#k uniqe picks from a list
lst = list(range(30))
e = random.choices(lst, k=10)
# print(e)

#shuffling a list randomly
random.shuffle(lst)
print(lst)

