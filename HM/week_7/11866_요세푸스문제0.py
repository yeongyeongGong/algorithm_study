N, K = map(int, input().split())

# 배열만들기
arr = [i for i in range(1, N + 1)]

# 시작지점 설정
front = 0

# 결과값
result = []

# 배열이 빌 때까지 반복
while arr:
    # K번째 값이 pop 될때마다 arr 길이가 줄어들기에 len(arr)로 나눔
    front = (front + (K - 1)) % len(arr)
    x = arr.pop(front)
    result.append(x)

print(f'<{', '.join(map(str, result))}>')