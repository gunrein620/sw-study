# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

rs = []

def make_tree(n, m):
  for i in range(n - (m-2) - 1):
    rs.append((i,i+1))
  for i in range(m-2):
    rs.append((1,n-(m-2)+i))
  return rs
n, m = map(int, input().split())
make_tree(n, m)
for a, b in rs:
  print(a, b)