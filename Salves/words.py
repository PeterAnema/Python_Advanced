
text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

text = text.lower().replace('.', '').replace(',', '').replace('!', '')
# or
# text = text.lower().translate(str.maketrans('','', '.,!:?;'))

words = text.split(' ')

unique_words = sorted(set(words))

print(unique_words)
print(len(unique_words))

# d = dict()
# for word in unique_words:
#     n = words.count(word)
#     if n > 1:
#         d[word] = n


d = {word: words.count(word) for word in sorted(set(words))}

print(d)

