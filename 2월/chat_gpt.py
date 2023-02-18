T = int(input())

def ts(N, A):
    while True:
        sorted = True
        for i in range(N-1):
            if A[i] > A[i + 1]:
                A[i] //= 2
                sorted = False
        if sorted:
            break

for i in range(T):
    N = int(input())
    A = list(map(int, input().strip().split()))
    ts(N, A)
    print(*A)