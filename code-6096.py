arr = []

for i in range(19):
    arr.append(list(map(int, input().split(' '))))

n = int(input())

point = []
for i in range(n):
    tmp = input().split(' ')
    tmp[0], tmp[1] = int(tmp[0])-1, int(tmp[1])-1
    point.append(tmp)

for i in range(n):
    j, k = point[i][0], point[i][1]
    for l in range(19): arr[j][l] = int(not arr[j][l])
    for l in range(19): arr[l][k] = int(not arr[l][k])

for i in range(19):
    for j in range(19):
        print(arr[i][j], end=' ' if j!=18 else '')
    print('')