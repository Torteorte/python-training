def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n < 0:
        return 1 / result
    return result


print(power(int(input()), int(input())))
