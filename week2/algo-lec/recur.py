def nsum(n):
  sum = 0
  for i in range(n):
    sum += n
  return sum 

def sum(n):
  if n == 0:
    return 0
  return n + sum(n-1)

print(sum(5))

#재귀특징
#  중간의 값을 알 수 없다. 
#  복귀하는 변곡점이 있다. 

#테일리커젼 
# 중간값 알 수 있고 복귀하는 변곡점 없다

def exp(b,n):
  if n == 0:
    return 1
  return b* exp(b,n-1)

def fast_expt(b,n):
  if n == 0:
    return 1
  else:
    if is_even(n):
      return square(fast_expt(b,n/2))
    else:
      return n * fast_expt(b, n-1)


def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:  
    return fib(n-1) + fib(n-2)

print(fib(5))

def change_combi(amount, coins):
  rs = []
  if amount == 0:
    return 1
  if amount < 0 or len(coins) == 0:
    return 0
  return