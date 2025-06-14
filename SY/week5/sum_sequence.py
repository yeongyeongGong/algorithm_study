def solution(sequence, k):
    n = len(sequence)
    left = 0
    total = 0
    min_len = n + 1
    answer = []

    for right in range(n):
        total += sequence[right]

        while total > k:
            total -= sequence[left]
            left += 1

        if total == k:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                answer = [left, right]

    return answer


if __name__ == "__main__":
    sequence = list(map(int, input().split()))
    k = int(input())
    print(solution(sequence, k))
