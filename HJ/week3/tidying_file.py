### 백준 20291 - 파일정리
'''
8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt

'''

N = int(input())
dict= {}

for n in range(N):
    tmp = input().split('.')[1]
    if tmp not in dict.keys():
        dict[tmp] = 1
    else :
        dict[tmp] += 1

for s in sorted(dict):
    print(s, end=' ')
    print(dict[s])

