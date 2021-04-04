def solution(X, A):
    map = {}
    second = 0
    while len(map) < X:
        map[A[second]] = True
        if len(map) == X:
            return second
        second += 1
        if second == len(A):
            return -1



print(solution(2, [1]))
