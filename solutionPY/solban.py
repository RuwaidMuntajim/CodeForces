k, n, w = map(int, input().split())
x = 1
money = 0

while x <= w and money != -1:
    money += k * x
    x += 1

money_toborrow = money - n
if money_toborrow >= 0:
    print(money_toborrow)
else:
    print(0)