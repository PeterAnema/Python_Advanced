import glob

for item in sorted(glob.glob('[abcd]*.py')):
    print(item)
