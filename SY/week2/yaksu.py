n = int(input()) # 약수 개수

numbers = list(map(int,input().split())) # 약수 입력 받기

N = max(numbers) * min(numbers) # 입력 받은 약수 중 가장 큰 수와 가장 작은 수를 곱한다

print(N) # N 출력 ..