### 백준 16196 - 중국 신분증 번호

'''
441323200312060636
1
441323

62012319240507058X
1
620123

321669197204300886
2
610111
659004

'''

from datetime import datetime

num = input()
N = int(input())
region=[]
for n in range(N):
    region.append(input())

## 지역번호 체크
if num[:6] not in region:
    print('I')
    exit()

## 생년월일 체크
birth = num[6:14]

try:
    dt = datetime.strptime(birth, '%Y%m%d')
except:
    print('I')
    exit()
else :
    if int(birth[:4]) < 1900 or int(birth[:4]) > 2011 :
        print('I')
        exit()

## 체크섬코드

fin=num[:17]
tmp= 0
times=17
for f in fin :
    tmp += int(f)*(2**times)
    times -= 1

x= 0
while True :
    if x == 11:
        print('I')
        exit()
    if (tmp + x) % 11 == 1 :
        break
    else :
        x +=1
if x == 10 :
    check = 'X'
else :
    check = str(x)

if check != num[-1]:
    print('I')
    exit()

if num[-4:-1] == '000':
    print('I')
    exit()

if int(num[-2]) % 2 == 0 :
    print('F')
else:
    print('M')

