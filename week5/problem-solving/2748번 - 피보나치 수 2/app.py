#=====================================================================
#   2748번:    피보나치 수 2                   
#   @date:   2026-03-28              
#   @link:   https://www.acmicpc.net/problem/2748  
#   @Note:   폴더 내부에 있는 파일을 삭제하거나 변경하지 말아주세요.
#   @Test:   코드를 작성 후 "BOJ: 테스트"통해서 테스트를 해보세요.
#=====================================================================

import sys;

input = sys.stdin.readline

def fib_memo(n, memo=None):
  if memo is None:
    memo = {}
  if n ==1 or n ==0:
    return n
  if n in memo:
    return memo[n]
  memo[n] = fib_memo(n-1,memo) + fib_memo(n-2, memo)
  return memo[n]

n = int(input())
print(fib_memo(n))