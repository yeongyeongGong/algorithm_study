# 복호화

T = int(input())

for tc in range(T):
    my_dict = {}  # 빈 dictionary 생성.
    lst = list(input())

    for i in range(len(lst)):  # 모든 글자를 dictionary 에 정리.
        if lst[i] == ' ':  # 빈 칸이면 패스.
            continue

        if lst[i] in my_dict:  # dictionary 에 있으면
            my_dict[lst[i]] += 1  # value 에 1을 추가.
        else:  # 없으면 value 를 1로 하여 추가.
            my_dict[lst[i]] = 1

    flag = 0  # 최댓값 찾기.
    for j in my_dict:
        if flag < my_dict[j]:
            flag = my_dict[j]
            e = j  # 최댓값을 찾으면서 그 문자도 찾음.

    cnt = 0
    for k in my_dict:  # 최댓값과 같은 값 갯수 찾기.
        if my_dict[k] == flag:
            cnt += 1

    if cnt > 1:  # 같은 게 두 개 이상이면
        print('?')  # ? 출력.
    else:  # 같은 게 하나라면
        print(e)  # 그 문자 출력.
