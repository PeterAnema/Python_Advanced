from datetime import date, datetime

d = date(2022, 3, 11)

print(d.strftime('%Y-%m-%d'))
print(d.isoformat())
print(d.strftime('%d-%m-%Y %H:%M'))

d = datetime.now()
print('Het is nu', d.strftime('%A %e %B %Y %H:%M'))
