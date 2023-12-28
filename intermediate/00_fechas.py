

from datetime import date
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


timestamp = now.timestamp()
print(timestamp)        # seconds from 1970

year_2023 = datetime(2023, 1, 1)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


timestamp = now.timestamp()
print(timestamp)


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.minute)
    print(date.second)


print_date(now)

year_2023 = datetime(2023, 1, 1, 12, 45)
print(year_2023)
print_date(year_2023)

print("--------------------------------------")


current_time = time(hour=23, minute=12, second=55)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("--------------------------------------")


print("--------------------------------------")

from datetime import timedelta

print(year_2023 -)

diff = year_2023-current_time
print(diff)
diff =year_2023.date() - current_time
print (diff)