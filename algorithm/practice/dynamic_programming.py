# 피보나치
def fibonacci(n):
    # 재귀 호출
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_dp(n):
    # 동적 프로그래밍
    cache = [0 for _ in range(n+1)]
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n]

if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci_dp(10))