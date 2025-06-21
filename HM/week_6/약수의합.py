# 프로그래머스 레벨 1
def solution(n):
    answer = 0
    for m in range(1, n + 1):
        if n % m == 0:
            answer += m
    return answer


n = int(input())
result = solution(n)
print(result)
