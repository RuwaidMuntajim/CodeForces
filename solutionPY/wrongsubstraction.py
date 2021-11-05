num, time = map(int, input().split())
t = 1

while t <= time:
    if num % 10 == 0:
        num = num / 10
    else:
        num -= 1
    t += 1

print(int(num))