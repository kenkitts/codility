def solution(A, B, K):
    count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            count += 1
    return count


def fast_solution(A, B, K):
    return B // K - (A - 1) // K


print(fast_solution(0, 0, 2))