def solution(A: list):
    A.sort()

    if A[0] != 1:
        return 0


    for i in range(len(A)-1):
        if A[i]+1 == A[i+1]:
            continue
        else:
            return 0
    return 1


print(solution([1,1,1,1]))