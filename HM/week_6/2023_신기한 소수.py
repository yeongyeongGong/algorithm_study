import math

# 소수 판별 함수
# 에라토스테네스의 채 사용
def isPrime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

# N자리 소수 구하기
def solve(l, num):
    if l == N:
        print(num)
        return
    for i in range(1, 10):
        # i가 짝수면 볼 필요도 없음
        if i % 2 == 0:
            continue
        # num * 10 + i이 소수라면 다음 자리로 이동
        if isPrime(num * 10 + i):
            solve(l + 1, num * 10 + i)


N = int(input())

# 맨 앞자리는 2, 3, 5, 7 가능
solve(1, 2)
solve(1, 3)
solve(1, 5)
solve(1, 7)
