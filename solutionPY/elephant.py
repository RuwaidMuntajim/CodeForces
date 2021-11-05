import time
global coord
coord = int(input(""))
x = 0
while x != -1:
    if coord == 0:
        print(x)
        break
    if coord - 5 > 0:
        coord -= 5
    elif coord - 4 > 0:
        coord -= 4
    elif coord - 3 > 0:
        coord -= 3
    elif coord - 2 > 0:
        coord -= 2
    elif coord - 1 > 0:
        coord -= 1
    print(coord)
    x += 1
