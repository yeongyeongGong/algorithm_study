# 첫번째 행렬
AN, AM = map(int, input().split())

A = []
for _ in range(AN):
    array = list(map(int, input().split()))
    A.append(array)

# 두번째 행렬
BN, BM = map(int, input().split())

B = []
for _ in range(BN):
    array = list(map(int, input().split()))
    B.append(array)

# 행렬 곱셈
# 행렬 C = A * B 일때
# C[1, 1] 원소 = A의 1행 원소들과 B의 1열 원소들을 매칭해 각각 곱한 뒤 더함
# B행렬 전차 시키기
transposed = [list(row) for row in zip(*B)]

C = [[0] * BM for _ in range(AN)]

for i in range(AN):
    array_A = A[i]
    for j in range(BM):
        array_B = transposed[j]
        C[i][j] = sum(a * b for a, b in zip(array_A, array_B))

for row in C:
    print(*row)