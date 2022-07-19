def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("10th term of the fibonacci series is:")
print(fibonacci(10))