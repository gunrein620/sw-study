
def fib_memo(n, memo=None):
  if memo is None:
    memo = {}
  if n ==1 or n ==2:
    return n
  if n in memo:
    return memo[n]
  memo[n] = fib_memo(n-1,memo) + fib_memo(n-2, memo)
  return memo[n]

n = int(input())

fib_memo(n)