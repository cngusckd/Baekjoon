import sys
N, P, Q = map(int,sys.stdin.readline().split()) # 문제 입력

def solution(N,P,Q): # recursion tree는 맞으나 baekjoon 검사에서는 시간초과.
    if N == 1 :
        return 2
    elif N == 0:
        return 1
    else:
        return solution(N//P,P,Q) + solution(N//Q,P,Q)


# DP로 풀기위해 dictionary 이용
dict = {}
dict[0] = 1

def solution(N):    # 시간초과 해결

    # A(n)값이 딕셔너리 있다면, 반환
    if (N in dict):
        return dict[N]
    # A(n)값이 딕셔너리에 없다면, recursion
    else:
        dict[N] = solution(N//P) + solution(N//Q)
        return dict[N]

print(solution(N))