def prefix_sum(A):
    n = len(A)
    P = [0] * (n+1)
    for i in range(1,n+1):
        P[i] = P[i-1] + A[i-1]
    return P


def count_total(P,x,y):
    return P[y+1] - P[x]


a = [1,2,3,4,5,6,7,8]

print(count_total(prefix_sum(a),3,5))
print(prefix_sum(a))
