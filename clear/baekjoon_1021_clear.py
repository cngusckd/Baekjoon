from collections import deque
import sys
input = sys.stdin.readline()
N , M = input.split()
N , M = int(N), int(M)
check = sys.stdin.readline()
check_list = check.split()
check_list = list(map(int,check_list))

count = 0

start_list = []
for i in range(1,N+1):
    start_list.append(i)

start_deque = deque(start_list)


answer = 0

while(count < M):
    target_index = start_deque.index(check_list[count])
    if(target_index == 0):
        count +=1
        start_deque.popleft()
        continue
    deque_len = len(start_deque)
    if(target_index > (deque_len//2)):
        rotate = deque_len - target_index  # 우측으로 rotate
        answer += rotate
    else:
        rotate = -target_index # 좌측으로 rotate
        answer -= rotate
    start_deque.rotate(rotate)
    start_deque.popleft()
    count += 1

print(f"{answer}")    