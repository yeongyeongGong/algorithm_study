T = int(input())
for _ in range(T):
    code = input().replace(" ", "")
    alphabet = dict()
    for c in code:
        # 알파벳이 딕셔너리에 있으면 1 증가, 없으면 키 추가-값은 0으로 초기화
        alphabet[c] = alphabet.get(c, 0) + 1

    max_count = max(alphabet.values())
    result = []
    for al, count in alphabet.items():
        if count == max_count:
            result.append(al)

    if len(result) > 1:
        print("?")
    else:
        print(result[0])