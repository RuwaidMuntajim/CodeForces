import time
K, r = map(int, input().split())
n = 1

while n != 0:
    if (K * n) % 10 == 0:
        time.sleep(2)
        print(n)
        time.sleep(2)
        break
    elif (K * n) % 10 == r:
        time.sleep(2)
        print(n)
        time.sleep(2)
        break
    n += 1
