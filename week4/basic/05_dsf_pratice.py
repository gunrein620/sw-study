def dfs(graph, start, visited=None):
  if visited is None: # <- 초기화 조건 
    visited = []
  
  visited.append(start) #<- 현재노드를 방문처리

  for node in graph[start]: #<- 앞으로 탐색할 노드 지정
    if node not in visited: # <- 처음 탐색된 노드 일 경우 
      dfs(graph, node,visited) # <- 해당노드의 끝지점까지 추적
  
  return visited

#테스트 
graph = {
  0: [1, 2],
  1: [0, 2],
  2: [0, 1, 3],
  3: [2]
}

rs = dfs(graph, 0)
print(rs)


