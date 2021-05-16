# 소수

- 1보다 큰 자연수 중 1과 자기자신으로만 나누어 떨어지는 수

### python

```py
def is_prime_number(n):
  for i in range(2, n):
    if n % i == 0:
      return False
 return True
```

### javascript

```js
function primecheck(n) {
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i == 0) return false;
  }
  return true;
}
```
