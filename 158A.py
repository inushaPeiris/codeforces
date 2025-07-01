input1 = str(input())
index_of_the_space = input1.find(' ') 
players_count = int(input1[:index_of_the_space])
pass_score = int(input1[index_of_the_space + 1:])

input2 = str(input())
scores = input2.split(' ')
pass_limit = int(scores[pass_score - 1])

result = 0

for scr in scores:
    if int(scr) >= pass_limit and int(scr) > 0:
        result += 1

print(result)
