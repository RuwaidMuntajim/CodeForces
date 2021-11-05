

name = input("")
list_name = list(name)
list_name.sort()
duplicate_name = []
print(list_name)

for x in list_name:
    if list_name.count(x) > 2:
        duplicate_name.append(x)
for a in duplicate_name:
    if duplicate_name.count(a) > 1:
        duplicate_name.remove(a)

print(duplicate_name)
#Under construction
