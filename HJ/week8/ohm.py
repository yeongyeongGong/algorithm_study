### 백준 1076 - 저항

'''
yellow
violet
red

4700
'''

value_dict = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9,
}

time_dict= {
    'black': 10**0,
    'brown': 10**1,
    'red': 10**2,
    'orange': 10**3,
    'yellow': 10**4,
    'green': 10**5,
    'blue': 10**6,
    'violet': 10**7,
    'grey': 10**8,
    'white': 10**9,
}

num_base= ''
first= input()
num_base += str(value_dict[first])
second = input()
num_base += str(value_dict[second])
final = input()
ans = int(num_base)*time_dict[final]
print(ans)