# 1. 첫째 줄에 두 개의 정수 n과 m이 주어진다. n은 펜션에서 관리하는 여름 성수기 총 기간을 나타내고, m은 펜션이 보유하고 있는 방의 개수이다(1≤n≤100, 3≤m≤30). 
# 편의상 성수기 기간을 1일부터 n일까지로 표시하고, 펜션의 방을 1부터 m까지의 번호로 구분한다.

# 2. 그 다음 n개의 줄에는 각 줄마다 길이가 m인 문자열이 주어진다. 입력에서 i+1 번째 줄의 j-번째 문자는 여름 성수기 기간 중 i-번째 날에 방 번호가 j인 
# 방의 예약 상태를 나타낸다(1≤i≤n, 1≤j≤m). 이 문자는 방이 이미 예약된 경우에는 'X', 그렇지 않으면 'O'이다. k-번째 날을 예약하면 그 다음 날 정오까지 
# 방을 사용할 수 있다는 것을 의미한다.

# 3. 마지막 줄에는 고객의 일정을 나타내는 두 개의 정수 s, t가 주어진다, s는 펜션에 도착하는 날이고 t는 펜션을 떠나는 날이다(1≤s<t≤n+1).

# 1. 첫째 줄에 예약 기간 동안 방을 옮기는 최소 횟수를 출력한다.

# 2. 만일, 방을 옮기지 않아도 되는 경우는 0, 예약이 불가능한 경우는 -1을 출력한다.

# 3. 고객이 1번 방, 2번 방, 1번 방을 차례로 이용하게 된다면 방을 두 번 옮긴 것으로 본다.

# 10 7
# XXXXXXX
# XOXXXXO
# XOXXXXO
# XOXXXOX
# OXXOXOX
# XOXOXOX
# OXXOXOX
# OXXXXOX
# XXXXXXX
# XXXXXXX
# 2 9

# N, M = map(int, input().split(' '))
# K , CNT = [], -1
# for i in range(N): K.append(list(input()))

# S, T = map(int, input().split(' '))
# S, T = S-1, T-1

# while(S<=T):
#     L = [0 for _ in range(M)]
#     for i in range(M):
#         if K[S][i] == 'O':
#             while(L[i]<T-S and K[S+L[i]][i]!='X'):
#                 L[i] = L[i]+1
#             if K[S+L[i]] == ['X' for _ in range(M)] and S+L[i] != T: L[i]=-1
#     B = 0
#     for i in range(1, M): 
#         if L[B] < L[i]: B = i
#     if L[B]>0:
#         S = S + L[B]
#         CNT = CNT + 1
#     else:
#         CNT = -1
#         break
# print(CNT)

n,m = map(int,input().split())


# 2.
info = [['X']*m] # 날짜를 편하게 확인하기 위해서 0번째 줄은 임의로 추가

for i in range(n):
    info.append(list(input()))


# 3. 손님이 머물 날
s, t = map(int, input().split())



# 4.


def check(n):

    maxday=0

    for i in range(m):
        day=0
        for j in range(n,t):
            if info[j][i]=='O':
                day+=1
            else:
                break

        if maxday<day:
            maxday=day
    return maxday


count=-1
today=s

while today<t:
    
    stay=check(today)

    if stay==0:
        count=-1
        break

    #print(stay)
    count+=1
    today+=stay

    


print(count)