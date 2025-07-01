limit = 10
input_count = int(input())
words = []

while input_count:
    word = input()
    words.append(word)
    input_count -= 1

for wrd in words:
    if len(wrd) > limit:
        mid_num = len(wrd) - 2
        print(f"{wrd[0]}{mid_num}{wrd[-1]}")
    else:
        print(wrd)
