# 프로그래머스 레벨 1
def solution(n):
    answer = 0
    for _ in range(len(n)):
        answer += (n % 10)
        n = n // 10

    # # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer
