### 백준 1564 - 팩토리얼5

'''
20

17664
'''

num = int(input())
num5 = 1
while num > 1 :
    num5 *= num
    num -= 1
    # 끝 0 제거
    while num5 % 10 == 0:
        num5 //= 10
    # 숫자 크기 제한
    num5 %= 10**12
    # 팩토리얼 값 자체는 보존하지 못하나, 끝자리만을 가지고 가기위한 연산
    # 지피티 > 끝자리 몇 개를 안정적으로 추적하면서도 계산이 빠르게 돌아갈 정도로 적절한 크기

str_num = str(num5)
for i in range(len(str_num)-1,-1,-1):
    if str_num[i] != '0':
        print(str_num[i-4:i+1])
        break

