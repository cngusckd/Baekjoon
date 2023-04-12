import sys

test_case_num = sys.stdin.readline()
test_case_num = int(test_case_num)
answer = []
for i in range(test_case_num):
    input =sys.stdin.readline().rstrip()
    a, b = input.split()
    a, b = int(a) , int(b)
    b = b % 4

    if(b==0):
        b=4
    remain = (a**b)%10
    if(remain == 0):
        answer.append(10)
    else:
        answer.append(remain)
for i in range(len(answer)):
    print(answer[i])