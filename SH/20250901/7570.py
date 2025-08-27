# 줄 세우기

# idea
# 순서대로 있지 않은 모든 숫자는 움직여야 함.
# 즉, 순서대로 있는 숫자 중 가장 긴 배열을 찾아
# 전체 갯수에서 그만큼을 빼면 답.
# 그럼, 그 순서대로 있는 숫자 중 가장 긴 배열을 어떻게 찾을 것인가?

N = int(input())

# 기존 배열과, 해당 배열의 숫자 위치를 저장할 배열 제작.
lst = list(map(int, input().split()))
pos = [0] * N

# lst 의 숫자 위치를 조사.
for i in range(N):
    pos[lst[i] - 1] = i

# 연속된 숫자의 길이를 확인.
cnt = 1
length = 1

# 연속된 숫자의 길이가 최장인 길이만 cnt에 저장.
for j in range(N - 1):
    if pos[j] < pos[j + 1]:
        length += 1
        cnt = max(cnt, length)
    else:
        length = 1

# 최장 길이를 제외한 나머지 인원은 모두 움직여야 함.
print(N - cnt)
