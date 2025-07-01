
from operator import contains


matrix = [[1,2,3], [3,1,2], [2,3,1]]

nums = matrix[0]

result = 0
for i in matrix:
    agg = 0

    for j in i:
        if contains(nums, j):
            agg += 1
    
    if agg == 3:
        result += 1

print('true') if result == 3 else print('false')
