from pathlib import Path

p = Path('.')

print('p.exists():', p.exists())
print('p.is_file():', p.is_file())
print('p.is_dir():', p.is_dir())
print('p.owner():', p.owner())

for item in sorted(p.glob('demo*.py')):
    print(item)

