def slow_solution(N: int, A: list):
    counters = [0] * N
    max_counter = 0
    for i in A:
        if 1 <= i <= N:
            if counters[i -1] < max_counter:
                counters[i -1] = max_counter +1
            else:
                counters[i -1] += 1
        elif i > N:
            max_counter = max(counters)
    for i, v in enumerate(counters):
        if v < max_counter:
            counters[i] = max_counter
    return counters


def fast_solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for K,X in enumerate(A): # O(M)
        if 1 <= X <= N:
            counters[X-1] = max(counters[X-1], last_update)
            counters[X-1] += 1
            max_counter = max(counters[X-1], max_counter)
        elif A[K] == (N + 1):
            last_update = max_counter

    for i in range(N): # O(N)
        counters[i] = max(counters[i], last_update)

    return counters


print(fast_solution(5, [3,4,4,6,1,4,4]))