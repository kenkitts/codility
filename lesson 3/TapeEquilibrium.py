def solution(A: list):
    p_map = dict()
    length = len(A)
    left = A[0]
    right = sum(A[1:length])
    p_map[1] = abs(left - right)
    if length == 2:
        return min(p_map.values())
    for p in range(2, length):
        left += A[p - 1]
        right -= A[p - 1]
        p_map[p] = abs(left - right)
    return min(p_map.values())


A = [3,1,2,4,3]
print(solution(A))


