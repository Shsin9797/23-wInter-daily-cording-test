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

    ----
    import sys


    def thanos_sort(A):
        n = len(A)
        while True:
            sorted = True
            for i in range(n - 1):
                if A[i] > A[i + 1]:
                    A[i] //= 2
                    sorted = False
            if sorted:
                break
        return A


    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))
        sorted_A = thanos_sort(A)
        print(*sorted_A)


----
T = int(input())

def thanos_sort(N, A):
    while not all(A[i] <= A[i+1] for i in range(N-1)):
        for i in range(N-1):
            if A[i] > A[i+1]:
                A[i] //= 2
    return A

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = thanos_sort(N, A)
    print(*sorted_A)


    ------

    T = int(input())


    def thanos_sort(A):
        if len(A) <= 1:
            return A
        else:
            mid = len(A) // 2
            left = thanos_sort(A[:mid])
            right = thanos_sort(A[mid:])
            i = j = 0
            sorted_list = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            sorted_list += left[i:]
            sorted_list += right[j:]
            return sorted_list


    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        sorted_A = thanos_sort(A)
        print(*sorted_A)



    ----

    T = int(input())


    def thanos_sort(N, A):
        if all(A[i] <= A[i + 1] for i in range(N - 1)):
            return A
        else:
            for i in range(N - 1):
                if A[i] > A[i + 1]:
                    A[i] //= 2
            return thanos_sort(N, A)


    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        sorted_A = thanos_sort(N, A)
        print(*sorted_A)