N = int(input())

for TC in range(1, N+1):
    length = int(input())
    str1 = input()
    str2 = input()
    correct = 0
    for i in range(length):
        if str1[i] == str2[i]:
            correct += 1

    print(f'#{TC} {correct}')