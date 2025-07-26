alphabet = {}

vocab = input()

for letter in vocab:
    check = letter.upper()
    if check not in alphabet:
        alphabet[check] = 1

    else:
        alphabet[check] += 1

max_char = [i for i,j in alphabet.items() if max(alphabet.values()) == j]
if len(max_char) > 1:
    print('?')

else:
    print(max_char[0])