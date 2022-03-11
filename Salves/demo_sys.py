import sys

print(f'{len(dir(sys))} items in {sys.__name__}')

for item in dir(sys):
    print(item)

print('sys.version:', sys.version)
print('sys.version_info:', sys.version_info)
print('sys.version_info.major:', sys.version_info.major)
print('sys.version_info.minor:', sys.version_info.minor)
print('sys.executable', sys.executable)
print('sys.platform', sys.platform)

print('sys.path')
for item in sys.path:
    print('    ', item)

print('Exiting with sys.exit()')
sys.exit()


