arr = []
for _ in range(10):
    arr.append(list(map(int, input().split(' '))))

x, y = 1, 1
while(arr[x][y]!=2 and (arr[x+1][y]!=1 or arr[x][y+1]!=1)):
    arr[x][y] = 9
    L = 1 if arr[x][y+1] != 1 else 0
    x, y = x + int(not L), y + L
arr[x][y] = 9

for i in range(10):
    for j in range(10):
        print(arr[i][j], end= ' ' if j!=9 else '')
    print('')