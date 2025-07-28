### 백준 17413 - 단어 뒤집기 2

'''
baekjoon online judge

<open>tag<close>

'''

word = input()

result=''
tmp_forward = ''
tmp_back = ''
for w in word:
    if w == '<':
        result += tmp_back[::-1]
        tmp_back=''
        tmp_forward += w
    if w == '>' :
        tmp_forward += w
        result += tmp_forward
        tmp_forward=''

    if tmp_forward !='' and w not in ('<','>'):
        tmp_forward += w

    if tmp_forward == '' and w not in ('<','>') and w != ' ':
        tmp_back += w
    if tmp_forward =='' and w == ' ':
        result += tmp_back[::-1]
        result += ' '
        tmp_back=''
result += tmp_forward
result += tmp_back[::-1]
print(result)
