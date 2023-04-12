import sys
input_line = sys.stdin.readline()
N, L = map(int, input_line.split())

start_num = 0
length = 0
check = False
for i in range(L, 101):
    temp = (N - (i-1)*i/2)
    if(temp%i == 0 and temp >= 0):
        check = True
        start_num = temp / i
        length = i
        break
if check:
    for i in range(int(start_num),int(start_num)+length):
        print(i,end=" ")
else:
    print(-1)