'''
import sys
input = int(sys.stdin.readline())
A = []
A.append(int(sys.stdin.readline()))
for i in range(input-1):
    input_num = int(sys.stdin.readline())
    check = True
    for j in range(len(A)):
        if A[j] > input_num:
            A.insert(j,input_num)
            check = False
            break
    if check : A.append(input_num)

print(A)
'''
import sys
input = int(sys.stdin.readline())
A = []
for i in range(input):
    A.append(int(sys.stdin.readline()))
A.sort()
for i in range(len(A)):
    print(A[i])