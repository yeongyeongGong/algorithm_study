# 식물의 기준
# 광합성을 하고, 운동성이 X
# P는 광합성, M은 운동성
# 즉 -> P는 O M은 X

N,M = map(int,input().split())  #N: 생물 종류수, M: 실험 수
# 실험결과를 기록해놓는 배열
plant = [''] * (N+1)

# 실험 결과에 따라서 식물인지 아닌지 숫자로 체크예정
# 광합성, 운동성 조건이 하나라도 반대이면
# 즉 P가 X이거나 M이 O인 식물은 숫자 3으로 기록
# 위에 해당하지 않는 식물 중 광합성과, 운동성 조건이 맞을 때마다 +1을 해줄거임
# 값이 3인 생물은 절대 식물이 될 수 없고
# 값이 2인 생물은 세종이의 기준에 의해서 식물에 해당
# 갑이 1 이하인 생물은 식물일 수도 아닐수도있음

# 최소값 -> 값이 2인 식물의 수 /  최대값 -> 값이 2 이하인 식물의 수
check = [0] * (N+1)
for _ in range(M):
    a,b,c = input().split()
    if int(c) == 0:
        plant[int(a)] += b+'X'
    else:
        plant[int(a)] += b+'O'

for i in range(1, N+1):
    if 'PO' in plant[i]:
        check[i] += 1
    elif 'PX' in plant[i]:
        check[i] = 3

    if 'MO' in plant[i]:
        check[i] = 3
    elif 'MX' in plant[i]:
        check[i] += 1
min_value = check.count(2)
max_value = sum(1 for j in check if j <= 2)
print(min_value, max_value - 1)

