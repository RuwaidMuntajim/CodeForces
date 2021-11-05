n = int(input(""))
i = 1
l = 0
while i <= n and l != -1:
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        l += 1
    i += 1
print(int(l))
