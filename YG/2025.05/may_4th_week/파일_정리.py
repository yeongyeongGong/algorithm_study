# 컴퓨터 파일을 정리할건데
# 확장자 기준으로 정리할거고
# 확장자별 파일 갯수 찾을거임
# 딕셔너리 써서 하나씩 돌면 되지않으려나,,?
# split써서 '.'을 기준으로 분리해서 입력값을 받고
# '.' 뒤에거 기준으로 딕셔너리에 키값 있으면
# value +1 없으면 키 추가하고 value -> 1 로 저장

N = int(input())
file = {}
for _ in range(N):
    file_name, extension = input().split('.')

    if not extension in file:
        file[extension] = 1
    else:
        file[extension] += 1

# 원래 내 코드
# file = dict(sorted(file.items()))
#
# for extension, value in file.items():
#     print(extension, value)

# gpt한테 딕셔너리 정렬 쉽게하는법 물어본 코드
for extension in sorted(file):
    print(extension, file[extension])