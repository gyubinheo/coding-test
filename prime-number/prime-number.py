import math
import time


# Prime Number : 1과 자기자신을 제외하면 자연수 중에서 어떤 숫자로도 나누어 떨어지지 않는 숫자 (ex. 2, 3, 5, 7,)
# 보통 자연수 n이 변수로 주어지고 n 이하의 소수 개수 or 소수 리스트를 구하는 문제가 자주 출제된다.

def use_loop(n):
    arr = [0, 0] + [1] * (n-1)
    for i in range(2, n+1):
        for j in range(2,i):
            if i % j == 0:
                arr[i] = 0
                break
    return [i for i, j in enumerate(arr) if j]

def use_eratosthenes(n):
    arr = [0, 0] + [1] * (n-1)
    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i]:
            for j in range(2*i, n+1, i):
                arr[j] = 0
    return [i for i, j in enumerate(arr) if j]

start = time.time()
use_loop(100000)
end = time.time()
print(f"use_loop: {end - start:.5f} sec")
start = time.time()
use_eratosthenes(100000)
end = time.time()
print(f"use_eratosthenes: {end - start:.5f} sec")
