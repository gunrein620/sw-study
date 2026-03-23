#=====================================================================
#   16173번:    점프왕 쩰리 (Small)                   
#   @date:   2026-03-23              
#   @link:   https://www.acmicpc.net/problem/16173  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

# 첫번째 입력 N 만큼의 정사각형 2차원 배열생성
# 배열에 각 정수들 대입 및 초기화 
# 시작조건 0,0 고정 목표지점 n-1,n-1 

n = int(input())
board = []

for i in range(n):
  row = list(map(int,input().split()))
  board.append(row)

start = (0,0)
end = (n-1, n-1)

def solve(r, c):
  if r == n-1 and c == n-1:
    return "HaruHaru"
  if r >= n or c >= n:
    return "Hing"
  if board[r][c] == 0:
    return "Hing"

  if solve(r, c + board[r][c]) == "HaruHaru":
    return "HaruHaru"
  if solve(r + board[r][c],c) == "HaruHaru":
    return "HaruHaru"
  
  return "Hing"

print(solve(0,0))

#==========다른 방식 ===========
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False]*N for _ in range(N)]

def dfs(r, c):
    if r == N-1 and c == N-1:
        return True
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    if visited[r][c]:
        return False
    
    visited[r][c] = True
    k = board[r][c]
    
    # 오른쪽 점프 또는 아래 점프
    if dfs(r, c + k) or dfs(r + k, c):
        return True
    
    return False

print("HaruHaru" if dfs(0, 0) else "Hing")

#
#**동작 과정 (예제 1):**
#```
#(0,0) 값=1
# ├─ 아래 (1,0) 값=1
# │   ├─ 아래 (2,0) 값=2
# │   │   ├─ 아래 (4,0) → 범위 밖 ✗
# │   │   └─ 오른쪽 (2,2) → -1 → 도착! ✓
# │   └─ ...
# └─ ...