import sys

A, B, V = sys.stdin.readline().split()
A, B, V = int(A), int(B), int(V)

up = A - B
answer = (V-B) // up

if answer*up == (V-B):
    print(answer)
else:
    print(answer+1)