from datetime import datetime
import time

dt = datetime(2021, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2021/01/01", '%Y/%m/%d')
dt = datetime.fromtimestamp(time.time())
# print(dt)
print(f"{dt.year}/{dt.month}/{dt.day}")
print(dt.strftime("%y/%B/%d"))



dt1 = datetime(2021, 1, 1)
dt2 = datetime.now()
print(dt2> dt1)