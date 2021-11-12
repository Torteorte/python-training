n = int(input())
maximum = 0
count_equal = 1

while n != 0:
    n = int(input())
    if maximum < n:
        maximum = n
    elif maximum == n:
        count_equal += 1

print(count_equal)
