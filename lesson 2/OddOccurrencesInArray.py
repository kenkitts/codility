def solution(A):
    if len(A) == 1:
         return A[0]
    A.sort()
    for i in range(0 , len (A) , 2):
         if i+1 == len(A):
             return A[i]
         if A[i] != A[i+1]:
             return A[i]

l = [1,2,3,4,5,6,1,2,3,4,5,6,7]
print(solution(l))

