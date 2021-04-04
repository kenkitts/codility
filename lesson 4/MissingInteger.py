def solution(A):
    counter = [0] * (max(A) + 1)

    for V in A:
        if V <= 0:
            continue
        counter[V-1] +=1

    for i in range(len(counter)):
        if counter[i] == 0:
            return i + 1

    return 1


print(solution([1,3,6,4,-1,-100,1,2]))