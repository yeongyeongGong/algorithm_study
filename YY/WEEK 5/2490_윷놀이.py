yutnori = {
    3:'A', 2:'B', 1:'C', 0:'D', 4:'E'
}

#배 = 0, 등 = 1
try:
    while True:
        yut = list(map(int,input().split()))

        cnt = 0
        for i in yut:
            if i == 1:
                cnt += 1

        result = cnt

        print(yutnori[result])

except EOFError:
    pass