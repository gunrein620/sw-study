from collections import deque

vertices = 4
edges = [(0,1), (0,2), (1,3)]

graph = {i: [] for i in range(vertices)}
in_degree = [0] * vertices

for start, end in edges:
    graph[start].append(end)
    in_degree[end] += 1

queue = deque()
for i in range(vertices):
    if in_degree[i] == 0:
        queue.append(i)

result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(result)