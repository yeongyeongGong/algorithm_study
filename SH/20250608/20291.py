# 파일 정리

N = int(input())
ext = dict()  # 확장자와 갯수를 정리할 dictionary.

for _ in range(N):
    file = list(input().split('.'))  # 파일 이름을 파일명과 확장자로 분할.
    if file[1] not in ext:  # 확장자가 딕셔너리에 없으면 추가.
        ext[file[1]] = 1
    else:  # 확장자가 있으면 갯수 추가.
        ext[file[1]] += 1

ext_list = list(ext)  # 확장자로만 이루어진 list.
ext_list.sort()  # 이름순 정렬.

for i in range(len(ext)):
    print(f'{ext_list[i]} {ext[ext_list[i]]}')  # 양식에 맞게 출력.