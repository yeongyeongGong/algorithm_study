def dfs(start, end, cnt=0):
    visited[start] = 1 # start 노드 방문 처리해주기

    if start == end: # 만약 start와 end 가 같다면 이미 도착한 것이므로, cnt를 return
        return cnt

    for node in graph[start]: # 현재 노드랑 연결되어 있는 노드 탐색 시작
        if visited[node] == 0: # 만약 해당 노드에 방문한적이 없다면
            temp = dfs(node, end, cnt + 1) # 재귀로 dfs 실행한 후 재귀로 호출된 dfs의 실행 결과 값을 temp에 저장
            if temp != -1: # 만약 재귀호출의 리턴값이 -1이 아니라면, start 노드에서 end 노드까지 갈 수 있다는 것이므로,
                return temp # temp를 리턴

    return -1 # 경로가 없다면 -1 리턴

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)] # 그래프 배열 생성 
visited = [0] * (n+1) # visited 배열 생성

for _ in range(m): # m번 반복 하면서 그래프 내용 담기
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = dfs(p1, p2) # dfs 함수 호출

print(result) # dfs 함수 실행 결과를 출력한다