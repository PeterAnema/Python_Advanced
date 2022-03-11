

filename = 'data.csv'

f = open(filename, 'w')

f.write('var1, var2, var3, n\n')
f.write('A, AA, u, 123\n')
f.write('B, AA, x, 23\n')
f.write('C, DD, a, 234\n')

f.close()

#------------------------------------------

filename = 'data.csv'

f = open(filename)

headers = f.readline().replace(', ',',').strip().split(',')
# or
# headers = map(str.strip, f.readline().strip().split(','))

for line in f:
    columns = line.replace(', ',',').strip().split(',')
    # or
    # columns = map(str.strip, line.strip().split(','))
    d = dict(zip(headers, columns))
    if d['var2'] == 'AA':
        print(d['var1'], d['n'])

f.close()
