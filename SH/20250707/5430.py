# AC

T = int(input())

for tc in range(T):

    p = list(input())
    n = int(input())
    is_empty = 0

    lst = input()
    if lst == '[]':
        lst = []
    else:
        lst = list(map(int, lst.strip().strip('[').strip(']').split(',')))

    is_reversed = 0
    start = 0
    end = len(lst) - 1

    for i in range(len(p)):
        if p[i] == 'R':
            is_reversed = (is_reversed + 1) % 2
        else:
            if not lst:
                is_empty = 1
                break
            else:
                if is_reversed:
                    end -= 1
                else:
                    start += 1

    end += 1

    if is_empty:
        print('error')
    else:
        if start > end:
            print('error')
        else:
            lst = lst[start:end]
            if is_reversed:
                lst.reverse()
            print('[' + ','.join(map(str, lst)) + ']')
