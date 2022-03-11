import math

user_input = input('Geef straal: ')

r = float(user_input)

area = math.pi * r ** 2

circumference = 2 * math.pi * r

print(r, area, circumference)

print('r = %.3f' % r)
print('area = %.3f' % area)
print('circumference = %.3f' % circumference)

print(f'r             = {r:10.3f}')
print(f'area          = {area:10.3f}')
print(f'circumference = {circumference:10.3f}')
