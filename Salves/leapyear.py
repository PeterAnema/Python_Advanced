user_input = input('Geef een jaartal: ')

year = int(user_input)

is_deelbaar_door_4 = year % 4 == 0
is_deelbaar_door_100 = year % 100 == 0
is_deelbaar_door_400 = year % 400 == 0

is_leapyear = (is_deelbaar_door_4 and not is_deelbaar_door_100) or is_deelbaar_door_400

is_leapyear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

y = year
print(not(y%4) and bool(y%100) or not(y%400))

print(year, is_leapyear)
