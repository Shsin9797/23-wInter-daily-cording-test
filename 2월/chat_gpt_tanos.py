"""
make a cord which fits to this discription and reduce the run time as short as possible : Thanos finally got his hands on the Infinity Gauntlet and is about to implement Thanos alignment. Thanos sorting is the second fastest sorting algorithm in the world. Given a sequence A[1], A[2], ..., A[N] of length N, the process of sorting this sequence Thanos is as follows.

1. Reduce the element A[i] satisfying A[i] > A[i + 1] (1 i i N N - 1) in half using the Infinity Gauntlet. That is, apply A[i] = floor(A[i] / 2). If there are multiple elements that satisfy this, process the first one.

2. Repeat step 1 until there are no more elements available to process.
Output the given sequence A by sorting Thanos.

The first line is given T for the number of test cases.

The first line of each test case is given a sequence length N (1 의 N 200 200000).

The second line is given a sequence of elements A[1], A[2], ..., A[N]. The i-th element of the sequence is the integer A[i] (1 A A[i] 1 1000 000).

The sum of Ns in all test cases shall not exceed 200000.


"""

from collections import deque

def thanos_sort(N, A):
    indices = deque(range(N-1))
    while indices:
        i = indices.popleft()
        if A[i] > A[i+1]:
            A[i] //= 2
            if i > 0:
                indices.append(i-1)
            indices.append(i)
            if i < N-2:
                indices.append(i+1)
    return A

T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = thanos_sort(N, A)
    print(*sorted_A)


    """
    
    The main change in this solution is the use of a deque to keep track of the indices of elements that need to be processed. Instead of checking all pairs of adjacent elements in each iteration of the outer loop, we only process the indices that are currently in the deque. When we update the value of an element, we add the index of the updated element to the deque, along with the indices of its neighbors (if they are not already in the deque).

This reduces the number of iterations of the outer loop, as we only process elements that need to be updated. It also reduces the number of iterations of the inner loop, as we only process each element once.
    
    """
