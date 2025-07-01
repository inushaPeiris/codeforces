problems_count = int(input())
words = []
result = 0

while (problems_count):
    words.append(str(input()))
    problems_count -= 1

for word in words: 
        if word == "++X" or word == "X++":
            result += 1
        if word == "--X" or word == "X--":
            result -= 1

print(result)
