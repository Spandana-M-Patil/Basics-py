import calendar
print('A month calendar:')
ans = int(input('Enter the year: '))
m = int(input('Enter the month: '))
# print(calendar.calendar(ans))
print(calendar.month(ans, m))
