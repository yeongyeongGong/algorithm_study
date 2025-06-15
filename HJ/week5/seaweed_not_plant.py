### 백준 30502 - 미역은 식물 아닌데요
'''
4 4
1 P 1
2 P 1
2 M 0
3 M 1

'''

# 광합성 하고, 운동성 없어야 식물
# N 생물 수, M 실험 수
N, M = map(int, input().split())

## 식물번호, 운동종류, 유무
## P 광합성, M 운동성. 1 True, 0 False

not_lst = set() # 확정적으로 안되는거
p_test=set()
m_test=set()
for m in range(M) :
    num, test, result = input().split()
    if (test == 'P' and int(result) == 0) or (test == 'M' and int(result) == 1 ) :
        not_lst.add(num)

    if test == 'P' and int(result) == 1 and num not in p_test :
        p_test.add(num)

    if test == 'M' and int(result) == 0 and num not in m_test :
        m_test.add(num)

real_lst = p_test & m_test # 확정적으로 되는거

print(len(real_lst), end=' ')
print(N-len(not_lst))

