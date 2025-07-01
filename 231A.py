from collections import Counter

problems_count = int(input())
words = []
result = 0

while (problems_count):
    words.append(str(input()))
    problems_count -= 1

for word in words: 
    freq = Counter(word)
    if freq['1'] >= 2:
        result += 1

print(result)
