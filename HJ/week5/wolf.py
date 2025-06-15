### 백준 13022 - 늑대와 올바른 단어

word = input()

while word :
    long= 0

    for i in word :
        if i == 'w' :
            long += 1
        else :
            break
    if long == 0 :
        print(0)
        exit()
    test = ''
    for t in 'wolf' :
        test += t * long
    if word[:len(test)] == test :
        word = word[len(test):]
    else :
        print(0)
        exit()
print(1)