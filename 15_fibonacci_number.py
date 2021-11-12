fib = int(input())

a = 0
b = 1
c = 0
count = 1

while c < fib:
    c = a + b
    a = b
    b = c
    count += 1

if c == fib:
    print(count)
else:
    print(-1)
