#=====================================================================
#   14244번:    트리 만들기                   
#   @date:   2026-03-20              
#   @link:   https://www.acmicpc.net/problem/14244  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline
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
    