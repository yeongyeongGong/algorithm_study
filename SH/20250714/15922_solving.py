# 아우으 우아으이야!!

N = int(input())

left = []
right = []

for _ in range(N):
    s, e = map(int, input().split())
    left.append(s)
    right.append(e)

start_point = 0
start = left[start_point]
end_point = 0
length = 0