import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
dice4 = random.randint(1, 6)
dice5 = random.randint(1, 6)

total = dice1 + dice2 + dice3 + dice4 + dice5

print(dice1, dice2, dice3, dice4, dice5)
print(str(dice1) + ' ' + str(dice2) + ' ' + str(dice3) + ' ' + str(dice4) + ' ' + str(dice5))
print('%d %d %d %d %d' % (dice1, dice2, dice3, dice4, dice5))
print('{} {} {} {} {}'.format(dice1, dice2, dice3, dice4, dice5))
print(f'{dice1} {dice2} {dice3} {dice4} {dice5}')

print('totaal aantal is ' + str(total))
print(f'totaal aantal is {total}')





# all_dice = []
# for _ in range(20):
#     gooi = random.randint(1, 6)
#     all_dice.append(gooi)
#
# total = sum(all_dice)
# print(all_dice)
# print('totaal aantal is ' + str(total))

