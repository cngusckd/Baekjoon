num = int(input())

answer = [[0 for col in range(100)] for row in range(100)]
for i in range(num):
    x,y = input().split()
    x,y = int(x),int(y)
    for j in range(10):
        for i in range(10):
            answer[x+i][y+j] = 1
count = 0
for i in range(100):
    for j in answer[i]:
        if j==1:
            count +=1
print(count)
'''
from itertools import combinations

num =  int(input())

answer = 100 * num

matrix = []

for i in range(num):
    x,y = input().split()
    x,y = int(x),int(y)
    matrix.append([x,y])


for i in list(combinations(matrix,2)):
    x1,x2 = max(i[0][0],i[1][0]), min(i[0][0],i[1][0])
    y1,y2 = max(i[0][1],i[1][1]), min(i[0][1],i[1][1])
    if((x1-x2>=10) or (y1-y2)>=10):
        continue
    answer -= (10 - (x1-x2))*(10 - (y1-y2))
print(answer)
'''