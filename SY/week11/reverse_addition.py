def reverse(num):
    result = ''
    n = len(num)
    for i in range(n-1, -1, -1):
        result += num[i]

    return result

X, Y = input().split()

reversed_x = reverse(X)
reversed_y = reverse(Y)

summation = int(reversed_x) + int(reversed_y)

print(int(reverse(str(summation))))