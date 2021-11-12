array = input().split()

a = [int(i) for i in array]
count = 0

for i in range(0, len(a)):
    if a[i - 1] != a[i]:
        count += 1

if count == 0:
    count += 1

print(count)
