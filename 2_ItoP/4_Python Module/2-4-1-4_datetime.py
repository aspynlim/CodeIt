import datetime

pi_day = datetime.datetime(2020, 12, 12, 18, 30, 33)
print(pi_day)        # 2020-12-12 18:30:33
print(type(pi_day))  # <class 'datetime.datetime'>
print(pi_day.strftime('%B %dth, %Y (%A)'))  # December 12th, 2020 (Saturday)
# string from time

today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=30, hours=10, minutes=50, seconds=33)

print(today)                 # 2020-12-17 16:07:43.742094
print(today + my_timedelta)  # 2021-01-17 02:58:16.742094
print(type(today))           # <class 'datetime.datetime'>
print(today.year)            # 2020
print(today.microsecond)     # 742094

print(today - pi_day)        # 4 days, 21:37:10.742094
print(type(today - pi_day))  # <class 'datetime.timedelta'>

