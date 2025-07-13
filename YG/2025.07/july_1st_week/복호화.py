T =  int(input())


for _ in range(T):
    sentence = list(input())

    letter = {}

    for i in range(len(sentence)):
        # 처음에 공백도 딕셔너리에 포함 해버려서
        # 공백의 빈도수가 젤 높은 경우가 생겨 틀렸음
        if sentence[i] != ' ':      # <- 해당 줄 추가하여 수정
            if sentence[i] in letter:
                letter[sentence[i]] += 1
            else:
                letter[sentence[i]] = 1


    max_val = max(letter.values())  #  딕셔너리에서 젤 큰 값 찾아서

    cnt = 0
    for k, v in letter.items(): # 빈도수 높은 철자가 여러갠지 확인
        if v == max_val:
            cnt += 1


    if cnt == 1:
        letter_e = max(letter,key=letter.get)
        print(letter_e)
    else:
        print('?')