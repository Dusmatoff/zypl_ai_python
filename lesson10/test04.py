import datetime

birthday = datetime.datetime(1995, 4, 7)

current_date = datetime.datetime.now()

days_passed = (current_date - birthday).days
print(days_passed)