import sys

N, K = map(int,sys.stdin.readline().split())

weight_and_value = []

for i in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    weight_and_value.append([weight, value])

def solution(i, N, K):
    if i < N-1:
        if K - weight_and_value[i][0] < 0:
            return 0
        else:
            return max(solution(i+1, N, K - weight_and_value[i][0]) + weight_and_value[i][1], solution(i+1, N, K))
    else:
        if K - weight_and_value[i][0] < 0:
            return 0
        else:
            return weight_and_value[i][1]
        
print(f"answer = {solution(0, N, K)} ")