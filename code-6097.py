h, w = map(int, input().split(' '))
arr = [[0 for _ in range(w)] for _ in range(h)]

n = int(input())
ldxy = []

for i in range(n):
    ldxy.append(list(map(int, input().split(' '))))

for i in range(n):
    for j in ldxy:
        k = 0
        for _ in range(j[0]):
            arr[j[2] + k * j[1] - 1][j[3] + k * int(not j[1]) - 1] = 1
            k = k + 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ' if j != w-1 else '')
    print('')