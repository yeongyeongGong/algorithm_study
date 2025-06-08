N = int(input())

repeat = star = N * 2 - 1
space = 0
reverse = False

for i in range(repeat):
    for _ in range(space//2):
        print(' ', end='')

    for j in range(star):
        print('*', end='')

    if not (i == repeat-1):
        print()

    if star == 1:
        reverse = True

    if reverse:
        star += 2
        space -= 2

    else:
        star -= 2
        space += 2