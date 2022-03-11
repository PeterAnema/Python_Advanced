import random

suits = ['clubs', 'diamonds', 'hearts', 'spades']

ranks = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')

deck = [s + ' ' + r  for s in suits for r in ranks]

random.shuffle(deck)

print(deck)

hand = [deck.pop() for _ in range(5)]

print(hand)
