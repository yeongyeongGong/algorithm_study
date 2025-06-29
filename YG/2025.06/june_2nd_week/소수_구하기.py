# M이상 N이하의 소수를 모두 출력
# 특정 숫자의 배수인 수를 지워나가면서 소수 판단 진행

M, N = map(int, input().split())

number = [True] * (N + 1)   # 모든 수를 소수로 가정
number[0] = number[1] = False   # 0,1은 소수가 아님

for i in range(2, int(N**0.5) + 1): # 소수인지 확인할 때 제곱근 이상의 범위까지 확인하는 것은 불필요
    if number[i]:
        for j in range(i * i, N + 1, i):    #M~N범위내에서 i의 배수는 소수가 아님
            number[j] = False

for i in range(M, N + 1):
    if number[i]:
        print(i)
