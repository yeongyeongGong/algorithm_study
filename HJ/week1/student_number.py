### 백준 - 학생 번호

T = int(input())
arr=[]
for t in range(T):
    arr.append(list(map(int, input())))

l = 0
result= 0
while True :
    l -= 1
    new_arr = []
    for now in arr:
        tmp = now[l:]
        if tmp not in new_arr :
            new_arr.append(tmp)
        else :
            break
    else :
        result = l * -1
        break
print(result)