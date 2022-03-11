
filename = 'data.csv'

f = open(filename)

headers = f.readline().replace(', ',',').strip().split(',')
print(headers)
print('----------------')

for line in f:
    columns = line.replace(', ',',').strip().split(',')
    d = dict(zip(headers, columns))
    if d['var2'] == 'AA':
        print(d['var1'], d['n'])

f.close()
