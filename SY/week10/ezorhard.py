N = int(input())
score_list = []
for _ in range(N):
    score = int(input())
    score_list.append(score)


min_score = score_list.index(min(score_list))
max_score = score_list.index(max(score_list))

if min_score == 0:
    print('ez')

elif max_score == 0:
    print('hard')

elif min_score != 0 and max_score != 0:
    print('?')