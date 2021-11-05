limak, bob = map(int, input().split())
year = 1

while year != 0:
    limak = limak * 3
    bob = bob * 2
    if limak > bob:
        print(year)
        break
    year = year + 1
