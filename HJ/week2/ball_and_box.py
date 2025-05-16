## SWEA - 공과 상자

'''

3
2 2 1 1 0
9 9 -11 -11 11
15 19 -2 4 -3

1
2 1 4 3 4

'''

T = int(input())
for t in range(T):
    b,w,x,y,z = map(int, input().split())
    result=[]

    score = 0

    while (b+w) > 0:
        if 2*z - (x+y) > 0 :
            same = min(b,w)
            b -= same
            w -= same
            score += same * z * 2
        elif max(x,y,z) == x and b:

            score += b * x
            b -= b
            score += w * y
            w -= w
        elif max(x,y,z) == y and w:
            score += w * y
            w -= w
            score += b * x
            b -= b


        if b == 0 and w :
            score += w * y
            w -= w
        elif w ==  0 and b:
            score += b * x
            b -= b

    print(score)

