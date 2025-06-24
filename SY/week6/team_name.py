def set_dict(name):
    variables = {ch: 0 for ch in 'LOVE'}
    for ch in name:
        if ch in variables:
            variables[ch] += 1
    return variables


eng_name = input()
N = int(input())

results = []

for _ in range(N):
    cand_name = input()
    variables = set_dict(eng_name)

    for ch in cand_name:
        if ch in variables:
            variables[ch] += 1

    vals = list(variables.values())
    tmp = 1
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            tmp *= (vals[i] + vals[j])

    percentage = tmp % 100
    results.append((percentage, cand_name))

# 사랑지수 내림차순, 이름 오름차순 정렬
results.sort(key=lambda x: (-x[0], x[1]))

print(results[0][1])
