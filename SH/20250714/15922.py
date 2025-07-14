# 아우으 우아으이야!!

# 처음 내 풀이.
N = int(input())

left = []
right = []

# 모든 정보를 받아 정리.
for _ in range(N):
    s, e = map(int, input().split())
    left.append(s)
    right.append(e)

# 포인터 설정.
pointer = 1
start = left[0]
end = right[0]
length = 0

# 포인터가 범위 내에 있을때만 반복.
while pointer < N:

    # 다음 선분의 시작점(왼쪽)이 이전 선분에 걸쳐있다면
    if start <= left[pointer] <= end:

        # 선분의 끝 지점을 새로 설정.
        if end < right[pointer]:
            end = right[pointer]
    
    # 다음 선분의 시작점(왼쪽)이 걸쳐있지 않다면
    else:

        # 선분 길이 추가하고, 새 시작점과 끝점을 설정.
        length += end - start
        start = left[pointer]
        end = right[pointer]

    # 포인터 이동.
    pointer += 1

# 마지막 케이스는 길이에 추가되지 않으므로 따로 추가.
length += end - start
print(length)



# 다른 사람 코드 참고하고 새로 푼 것.
# list 를 만들고 append 하고 어쩌고 할 필요가 없다.
N = int(input())

length = 0

# 시작점과 끝점을 제일 처음 값으로 설정.
s, e = map(int, input().split())

# N - 1 개의 값을 반복.
for _ in range(N - 1):

    # 새 값을 받아서
    ns, ne = map(int, input().split())

    # 그 전 선분과 시작점이 겹치면 끝 점을 수정.
    if ns <= e:
        e = max(e, ne)
    
    # 겹치지 않으면 그 전 선분을 계산 후 시작점, 끝점을 재설정.
    else:
        length += e - s
        s, e = ns, ne

# 마지막 케이스가 입력되지 않으므로 추가.
length += e - s

print(length)