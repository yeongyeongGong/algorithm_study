def solution(order):
    answer = 0
    n = len(order)
    cb = [i for i in range(1, n + 1)]  # 메인 컨베이어: 1부터 N까지
    sub_cb = []  # 보조 컨베이어 (스택)
    idx = 0  # order 순회 인덱스

    for box in cb:
        sub_cb.append(box)

        while sub_cb and sub_cb[-1] == order[idx]:
            sub_cb.pop()
            answer += 1
            idx += 1
            if idx == n:
                break

    return answer


if __name__ == "__main__":
    order = list(map(input().split()))
    print(solution(order))