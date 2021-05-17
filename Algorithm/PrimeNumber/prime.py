# 개념적 알고리즘
def is_prime_number(m):
  for i in range(2, m):
    if m % i == 0:
      return False
  return True

print(is_prime_number(121)) # false
print(is_prime_number(17)) # true

# 단점 : 모든 수를 계산해봐야하기 떄문에 효율이 떨어진다 => O(n)
'''
약수를 활용해보자!!!
ex) 16이 소수인지 판단해보자
    16의 약수 = 1, 2, 4, 8, 16 
      ===> 짝을 지어보면 (1, 16), (2, 8), (4, 4), (8, 2), (16, 1) => 가운데 값을 기준으로 반만 비교해보면 된다
           ===> 2 ~ 4까지만 나누어 보면 된다
'''

# 약수를 이용한 알고리즘
import math

def is_prime_number2(n):
  for i in range(2, int(math.sqrt(n)) + 1): # sqrt() : 제곱근
    if n % i == 0:
      return False
  return True

print(is_prime_number2(171)) # false
print(is_prime_number(19)) # True

# O(n^1/2)