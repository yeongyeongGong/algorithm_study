alpha_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0,
            'e': 0, 'f': 0, 'g': 0, 'h': 0,
            'i': 0, 'j': 0, 'k': 0, 'l': 0,
            'm': 0, 'n': 0, 'o': 0, 'p': 0,
            'q': 0, 'r': 0, 's': 0, 't': 0,
            'u': 0, 'v': 0, 'w': 0, 'x': 0,
            'y': 0, 'z': 0}

def dict_reset():
    for alpha in alpha_dict.keys():
        alpha_dict[alpha] = 0


N = int(input())

for _ in range(N):
    dict_reset()
    sentence = input()
    for letter in sentence:
        if letter != ' ':
            alpha_dict[letter] += 1

    max_value = max(alpha_dict.values())
    max_keys = [k for k, v in alpha_dict.items() if v == max_value]

    if len(max_keys) == 1:
        print(max_keys[0])
    else:
        print('?')