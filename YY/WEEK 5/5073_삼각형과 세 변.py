try:
    while True:
        a,b,c = map(int,input().split())

        if a==0 and b==0 and c==0:
            continue

        sides = sorted([a,b,c])
        if sides[0]+sides[1] <= sides[2]:
            print('Invalid')

        elif a==b==c:
            print('Equilateral')

        elif a==b or a==c or b==c:
            print('Isosceles')

        else:
            print('Scalene')

except EOFError:
    pass
# 7 7 7
# 6 5 4
# 3 2 5
# 6 2 6
# 0 0 0