array = input().split()

a = [int(i) for i in array]
index_max = 0

for i in range(0, len(a)):
    if a[i] > a[index_max]:
        index_max = i
print(a[index_max], index_max)
