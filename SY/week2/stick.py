X = int(input()) # 원하는 길이
length = 64 # 막대 길이
count = 0 # 막대 개수

while X > 0: # X가 0보다 큰 동안 아래의 과정을 반복한다:
    if length <= X: # length가 X보다 작다면:
        X -= length # X에서 length 만큼 빼준다
        count += 1 # == 막대 한개 사용 했으므로 count 증가

    length //= 2 # 만약 위 조건문에 걸리지 않았다면, 막대를 반으로 자른다

print(count) # 반복문 종료 후 count 출력
