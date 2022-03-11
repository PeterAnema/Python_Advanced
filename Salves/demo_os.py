import os

print(f'{len(dir(os))} items in {os.__name__}')

for item in dir(os):
    print(item)

current_working_directory = os.getcwd()
print('os.getcwd():', os.getcwd())
print('os.chdir to ..')
os.chdir('..')
print('os.getcwd():', os.getcwd())
os.chdir('/Users/peter')
print('os.getcwd():', os.getcwd())
os.chdir(current_working_directory)
print('os.getcwd():', os.getcwd())

# in Microsoft Windows
try:
    os.chdir('C:\\Users\\Peter')
    os.chdir(r'C:\Users\Peter')
    os.chdir('C:/Users/Peter')
except:
    print('You\'re not on Windows')

print('os.listdir():')
for item in sorted(os.listdir()):
    if item.endswith('.py'):
        print('    ', item)

print('os.path.exists(\'cards.py\')', os.path.exists('cards.py'))