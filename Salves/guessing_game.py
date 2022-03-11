import random

secret_number = random.randint(1, 100)

print('Raad een getal tussen 1 en 100')

teller = 0
while True:
    gok = int(input('Wat denk je dat het getal is? '))
    teller += 1

    if gok == secret_number:
        print(f'YEAH! Je hebt het in {teller} keer geraden.')
        break

    elif gok > secret_number:
        print('lager')

    elif gok < secret_number:
        print('hoger')

