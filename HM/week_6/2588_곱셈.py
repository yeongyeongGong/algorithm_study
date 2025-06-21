num1 = int(input())
num2 = input()
for n in range(1,len(num2)+1):
    print(num1 * int(num2[len(num2) - n]))
print(num1 * int(num2))