from operator import index

n = int(input())

cup = [1,2,3]
for i in range(0,n):
    a,b = map(int,input().split())
    # print(a,b)

    a_idx = cup.index(a)
    b_idx = cup.index(b)

    cup[a_idx],cup[b_idx]= cup[b_idx],cup[a_idx]

# print(cup)
print(cup[0])

