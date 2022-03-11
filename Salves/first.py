magicnumber = 11

print('break')
for i in range(1, 21):
    if i == magicnumber:
        break
    print(i)

print('continue')
for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
