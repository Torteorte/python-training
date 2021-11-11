f = int(input())
result = 0

for i in range(1, f + 1):
    r = 1
    for j in range(1, i + 1):
        r *= j
    result += r

print(result)
