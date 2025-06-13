N = int(input())
extensions = dict()
for _ in range(N):
    file, extension = map(str, input().split('.'))
    if extension in extensions:
        extensions[extension] += 1
    else:
        extensions.setdefault(extension, 1)

sorted_extensions = sorted(extensions.items())

for e, c in sorted_extensions:
    print(e, c)
