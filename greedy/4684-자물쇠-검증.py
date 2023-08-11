N = int(input())

arr = [i+1 for i in range(N)]

print(arr)

N1 = int(input())
N2, N3 = map(int, input().split(' '))
N4 = int(input())

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

push(N1)
reverse(N2-1, N3-1)
push(N4)
print(arr)