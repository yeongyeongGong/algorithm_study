n = int(input())
r= 5

#ㅁ의 윗부분
x = ('@'*n*r)
for i in range(n):
    print(x)

#ㅁ의 중간부분
#1 2 3 13 14 15 => @
#4 5 6 7 8 9 10 11 12 => ' '
y = ('@'*n)
result1 = ''
result2 = ''
result3 = ''
for j in range(n*r): #인덱스는 0부터 n-1까지 있음.
    #첫 부분 @
    if j<n: #주어진 n보다 작으면 @
        result1 += '@'

    #중간 부분 ' '
    if n<j<=n*4:
        result2 += ' '

    #끝 부분 @
    if j >= n*4:
        result3 += '@'

middle = (result1+result2+result3)

for k in range(n*3):
    print(middle)

#ㅁ의 끝부분
z = ('@'*n*r)
for i in range(n):
    print(z)