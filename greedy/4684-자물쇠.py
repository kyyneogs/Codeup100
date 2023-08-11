N = int(input())
arr = list(map(int, input().split(' ')))
print(arr)

def find_push():
    m1, m2, n, p1, p2 = 0, 0, 0, 0, 0
    while(True):
        if n+1>N-1: break
        if (arr[n+1] == arr[n]+1) or (arr[n+1]==arr[n]//N): 
            m1 = m1+1
            if m1 == 1: p1=n
        else:
            m1 = 0
        n = n+1
        if m1 > m2:
            m2 = m1
            p2 = p1
    return p2

def find_stop_point(reverse=False):
    p, n= 0, 0
    while(n+1<N):
        if (arr[n+1]==arr[n]+1 or (reverse and arr[n+1]==arr[n]//N)): n = n+1
        else:
            p=n
            break
    return p+1

def push(K):
    for i in range(K):
        tmp = arr[0]
        for j in range(1,N): arr[j-1]=arr[j]
        arr[N-1]=tmp

def reverse(K1, K2):
    for i in range(K2-K1):
        arr[K1], arr[K2] = arr[K2], arr[K1]
        K1, K2 = K1+1, K2-1
        if K1>=K2: break

A1 = find_push()
push(A1)

A2 = find_stop_point(reverse=True)
reverse(A2, N-1)

A3 = find_stop_point()
push(A3)

print(N-A3)
print(A2+1, N)
print(N-A1)