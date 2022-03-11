import re

s = 'dit is tekst met peter@tip.nl en zo richard@xs4all.nl rrr'

pattern = r'(\w+@\w+\.\w{2,3})'

regex = re.compile(pattern)

matches = regex.findall(s)

if matches:
    for match in matches:
        print(match)

