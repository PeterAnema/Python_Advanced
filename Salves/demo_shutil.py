import shutil

print(f'{len(dir(shutil))} items in {shutil.__name__}')

for item in dir(shutil):
    print(item)

print('shutil.disk_usage(\'.\')', shutil.disk_usage('.'))
