import sys

N, K = map(int,sys.stdin.readline().split())

weight_and_value = []

for i in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    weight_and_value.append([weight, value])

weight_and_value.sort(key = lambda x:x[0])  # 일단 key값 기준으로 오름차순 정렬시킴 ( WEIGHT 값 기준으로 )

answer = []
for i in range(N):
    if i == 0:
        answer.append([weight_and_value[0],K - weight_and_value[1], 0, K])