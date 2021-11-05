total_word = int(input(""))
n = 1
words = []
sh_word = []
while n <= total_word:
    word = input("")
    words.append(word)
    n += 1
for word in words:
    if len(word) <= 10:
        sh_word.append(word)
    else:
        a = word[0]
        x = word[-1]
        r = len(word[1:-1])
        new_word = f"{a}" + f"{r}" + f"{x}"
        sh_word.append(new_word)
for word in sh_word:
    print(word)
