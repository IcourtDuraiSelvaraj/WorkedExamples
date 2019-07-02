from datetime import datetime as dt

for i in range(0,5):
    print(dt.now())

print(dt(2019, 7, 2))
print(dt(2019, 7, 2, 14, 11, 55))

if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
    print("Working hours....")
else:
    print("fun hours")