# 입력받을 문자를 전부 대문자로 바꿔서 받기
words = list(input().upper())

counts = {}
for w in words:
    # 만약 counts에 문자가 있으면 개수 증가
    # counts에 문자가 없으면 추가
    counts[w] = counts.setdefault(w, 0) + 1

# 최대 개수 문자 찾기
sorted_counts = sorted(counts.items(), key=lambda x: x[1])
# 최대 개수인 문자가 여러개인 경우(마지막 문자의 개수와 그 앞의 문자 개수가 같은 경우)
if len(sorted_counts) > 1 and sorted_counts[-1][1] == sorted_counts[-2][1]:
    print('?')
else:
    print(sorted_counts[-1][0])
