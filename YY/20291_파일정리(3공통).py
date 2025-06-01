n = int(input())

files =[]
for i in range(n):
    file = input().split('.')
    # print(file)
    files.append(file[1])

ext = []
for j in files:
    if j not in ext:
        ext.append(j)

# print(ext)
for extension in ext:
    print(extension,files.count(extension))


