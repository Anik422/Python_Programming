from datetime import datetime, timedelta

dt1 = datetime(2021, 2, 18) + timedelta(days=1, seconds=4)
print(dt1)
dt2 = datetime.now()
 
duration = dt2 - dt1
print(duration)
print("Days :",duration.days)
print("Seconds :",duration.seconds)
print("total seconds :",duration.total_seconds())