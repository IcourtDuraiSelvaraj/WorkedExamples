import time

print(time.time())

print(time.asctime())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

for i in range(0,5):
    print(i)
    time.sleep(1)