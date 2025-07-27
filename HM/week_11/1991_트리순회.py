'''
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''


def preOrder(now):
    if now == '.':
        return
    print(now, end='')
    preOrder(tree[now][0])
    preOrder(tree[now][1])


def inOrder(now):
    if now == '.':
        return
    inOrder(tree[now][0])
    print(now, end='')
    inOrder(tree[now][1])


def postOrder(now):
    if now == '.':
        return
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end='')


tree = {}

N = int(input())
for i in range(1, N + 1):
    root, left, right = input().split()
    tree[root] = [left, right]


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
