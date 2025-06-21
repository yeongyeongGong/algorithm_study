a = int(input())
b = int(input())
c = int(input())

result = a + b + c

if result != 180:
    print('Error')

elif result == 180 and a == 60 and b == 60 and c == 60:
    print('Equilateral')

elif result == 180 and (a==b or a==c or b==c):
    print('Isosceles')

elif result == 180 and a != b and a !=c and b != c:
    print('Scalene')

