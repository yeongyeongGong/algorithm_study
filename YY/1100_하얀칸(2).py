chess = [['.']*8 for _ in range(8)]

for k in range(8):
    data = list(map(str,input().strip()))

    for i in range(8):
        if data[i] == 'F':
            chess[k][i] = 'F'

# print(chess)

count = 0
for r in range(8):
    for c in range(8):
        #하얀 칸은 (짝,짝) or (홀,홀)임.
        if (r%2 == 0 and c%2 == 0 and chess[r][c]=='F') or (r%2 == 1 and c%2==1 and chess[r][c]=='F'):
            count += 1

print(count)