alphabet = 'abcdefghijklmnopqrstuvwxyz'

N = int(input())

for TC in range(1, N+1):
    sentence = input()
    cnt = 0
    for i in range(len(sentence)):
        if sentence[i] == alphabet[i]:
            cnt += 1
        else: break

    print(f'#{TC} {cnt}')