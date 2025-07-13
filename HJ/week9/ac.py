## 백준 5430 - AC


T = int(input())
for _ in range(T):
    command = input()
    n = int(input())
    lst = eval(input())
    command = command.replace('RR','')


    isLeft = True # 왼 > 오

    for c in command:
        if c == 'R':
            isLeft = not isLeft
        if c == 'D':
            if len(lst) != 0 :
                if isLeft:
                    lst.pop(0)
                else :
                    lst.pop()
            else :
                print('error')
                break
        # print(lst)
    else :
        if isLeft :
            str_lst=str(lst)
        else :
            lst.reverse()
            str_lst= str(lst)
        str_lst = str_lst.replace(' ', '')
        print(str_lst)