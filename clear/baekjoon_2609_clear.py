import sys
input = sys.stdin.readline()
A, B = input.split()
A, B = int(A), int(B)

def GCD(A, B):

    if A>B:
        max = A
        min = B
    else:
        max = B
        min = A
    if(max % min == 0):
        return min
    else:
        return GCD(max%min, min)

gcd = GCD(A,B)
print(gcd)
print(A*B//gcd)