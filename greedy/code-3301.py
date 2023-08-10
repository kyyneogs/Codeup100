# 어떤 가게의 욕심쟁이 점원은 거스름돈을 나눠줄때 거스름돈의 개수를 적게해서 주고자 한다.

# 거스름돈을 입력 받아 점원이 줄 수 있는 최소 거스름돈의 개수를 출력하시오.

# 예를 들어 54520원인 경우,

# 거스름돈으로 50000원권 1장, 1000원권 4장, 500원 1개, 10원 2개 해서 총 8개이다.

# (※ 현재 우리나라가 사용하고 있는 화폐를 사용한다. 10원 50원 100원 500원 1,000원 5,000원 10,000원 50,000원)

# 거스름돈 n이 입력된다. ( n은10이상의  int 범위 )

# 내 코드는 쓰레기야...

# 나의 원숭이 같던 아이디어 : 우끼끼 ~ (오만원 넘을때마다 한장씩, 만원 넘길때마다 한장씩 ~ 계속 반복, 시간 오래걸림)

# N = int(input())
# C = 0
# while(N>0):
#     if N//50000>0: N = N-50000
#     elif N//10000>0: N = N-10000
#     elif N//5000>0: N = N-5000
#     elif N//1000>0: N = N-1000
#     elif N//500>0: N = N-500
#     elif N//100>0: N = N-100
#     elif N//50>0: N = N-50
#     elif N//10>0: N = N-10
#     else: break
#     C = C+1
# print(C)

# 누군가의 똑똑한 아이디어 : 그냥 오만원으로 바꿀수 있는거 다 바꾼다음에, 바로 만원으로 바꿀 수 있는것도 다 바꾸고 효율적으로 하자.

N = int(input())
C = 0
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in money:
    C += N//i
    N = N%i
print(C)