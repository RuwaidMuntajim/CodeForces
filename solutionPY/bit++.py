n = int(input(""))
l = 0
x = 1
while x <= n:
    sign = input("")
    if sign == "X++" or sign == "++X":
        l += 1
    elif sign == "X--" or sign == "--X":
        l -= 1
    x += 1
print(l)