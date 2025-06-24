
n = int(input())

r = 5

# 5-1=4 칸빠짐 => 1 * 4칸
# 15-3=12 칸빠짐  => 3 * 4칸


#ㄷ의 윗부분
x = ('@'*n*r)
for i in range(n):
    print(x)

#ㄷ의 세로부분
y = ('@'*(n*r-4*n))
for j in range(n*3):
    print(y)

#ㄷ의 아랫부분
z = ('@'*n*r)
for i in range(n):
    print(z)