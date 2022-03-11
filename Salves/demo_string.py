import string

s = 'This  is a beautiful example of random text'

trans = str.maketrans('ia', 'AI', 'x')
result = s.translate(trans)

print(result)

print(string.ascii_letters)

print('\u27B7')