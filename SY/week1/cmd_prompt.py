# N = int(input())
#
# string = [input() for _ in range(N)]
#
# diff = {}
# for i in range(N):
#     base = string[i]
#     temp = set()
#     for j in range(N):
#         if i == j : continue;
#
#         comp = string[j]
#
#         for k in range(len(base)):
#             if base[k] != comp[k]:
#                 temp.add(k)
#
#     diff[i] = list(temp)
#
# min_key = min(diff, key=lambda x: len(diff[x]))
#
# base = string[min_key]
# str_diff = set()
# for i in range(N):
#     if i == min_key : continue
#
#     comp = string[i]
#     for j in range(len(base)):
#         if base[j] !=  comp[j]:
#             str_diff.add(j)
#
# str_diff = list(str_diff)
#
# base = list(base)
# for num in str_diff:
#     base[num] = '?'
#
# final = ''.join(base)
#
# print(final)

N = int(input())
strings = [input() for _ in range(N)]

result = []

for chars in zip(*strings):
    if all(c == chars[0] for c in chars):
        result.append(chars[0])
    else:
        result.append('?')

print(''.join(result))













