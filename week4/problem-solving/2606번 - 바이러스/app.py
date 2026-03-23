#=====================================================================
#   2606번:    바이러스                   
#   @date:   2026-03-23              
#   @link:   https://www.acmicpc.net/problem/2606  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

from collections import deque
import sys;

input = sys.stdin.readline

# 초기입력 값 컴퓨터대수 = n | 네트워크연결쌍 수 = m
n = int(input())
m = int(input())
graph = {i: [] for i in range(1,n+1)} # 입력받은 수 많큼 그래프 초기화

# 그래프 채우기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# 탐색준비 완료 
# BFS 탐색시도

visited = [1]
que = deque([1])

while que:
  node = que.popleft()
  for i in graph[node]:
    if i not in visited:
      que.append(i)
      visited.append(i)
print(len(visited)-1)





