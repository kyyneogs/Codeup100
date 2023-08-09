# python 언어에서 가장 기본적인 명령이 출력문이다.
# print( )를 이용해 다음 단어를 출력하시오.

# Hello

# 참고
# 아래와 같은 소스 코드를 작성하고 실행시키면,
# 지정한 "문장"이 출력(print)된다.
# print("문장") 

# ** 주의 : 본 화면에서 복사하여 붙여넣기하면 제대로 되지 않을 수 있으니 직접 소스코드를 작성해 넣어야 한다.

# 000907-1121112

# n = input().split(' ')
# for i in range(len(n)): n[i] = int(n[i])
# for i in n:
#     if i//3==1: print('spring')
#     elif i//3==2: print('summer')
#     elif i//3==3: print('fall')
#     else: print('winter')

# n = input().split(' ')
# for i in range(len(n)): n[i] = int(n[i])

# for i in range(n[0]):
#     for j in range(n[1]):
#         print(i+1, j+1, sep=' ')


# arr = [[0 for _ in range(19)] for _ in range(19)]
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