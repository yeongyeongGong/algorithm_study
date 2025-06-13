def search_number(start, end, number):
    # 이진탐색 이용
    if start > end:
        print(0)
        return
    m = (start + end) // 2
    if A[m] == number:
        print(1)
        return
    if number > A[m]:
        search_number(m + 1, end, number)
    if number < A[m]:
        search_number(start, m - 1, number)


N = int(input())
A = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

# A 정렬하기
A = sorted(A)
for n in numbers:
    search_number(0, N - 1, n)

