from test1 import  abc
import datetime

now_time = datetime.datetime.now()
print(now_time.date().year)

while True:
    if now_time.date().year == 2019:
        print('123')