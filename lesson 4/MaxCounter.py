def solution(N: int, A: list):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for K, X in enumerate(A):
        if 1 <= X <= N:
            counters[X-1] = max(counters[X-1], last_update)
            counters[X-1] = counters[X-1] + 1
            max_counter = max(counters[X-1], max_counter)
        elif X == N+1:
            last_update = max_counter

    for i in range(N):
        if counters[i] < max_counter:
            counters[i] = last_update

    return counters


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
