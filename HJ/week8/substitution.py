### 백준 9046 - 복호화

'''
3
asvdge ef ofmdofn
xvssc kxvbv
hull full suua pmlu

'''

origin = 'abcdefghijklmnopqrstuvwxyz'
change = 'wghuvijxpqrstacdebfklmnoyz'

N = int(input())
for n in range(N):
    string = input().strip()
    new_string =''
    for s in string:
        if s in origin :
            new_string += change[origin.index(s)]
    char=dict()
    for i in new_string:
        if i in char.keys():
            char[i] += 1
        else :
            char[i] = 1

    many=[]
    for c in char.items():
        if c[1] == max(char.values()):
            many.append(c[0])
    if len(many) != 1 :
        print('?')
    else :
        print(origin[change.index(many[0])])


