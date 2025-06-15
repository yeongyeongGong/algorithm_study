N = int(input())

exts = {}
file_names = [input() for _ in range(N)]

for file_name in file_names:
    idx = file_name.rfind('.')
    tmp = file_name[idx+1:]

    if tmp not in exts:
        exts[tmp] = 1

    else:
        exts[tmp] += 1

for ext in sorted(exts):
    print(ext, exts[ext])