def distance(A, B):
    N, m = len(A), len(B)
    if N > m:
        A, B = B, A
        N, m = m, N

    a = range(N+1)
    for j in range(1, m+1):
        previou, a = a, [j]+[0]*N
        for g in range(1,N+1):
            ad, c, CHANGE = previou[g]+1, a[g-1]+1, previou[g-1]
            if A[g-1] != B[j-1]:
                CHANGE += 1
            a[g] = min(ad, c, CHANGE)

    return a[N]

a = input()
b = input()
print(distance(a, b))
