array = input().split()

a = [int(s) for s in array]
index_min = 0
index_max = 0

for i in range(1, len(a)):
    if a[i] > a[index_max]:
        index_max = i
    if a[i] < a[index_min]:
        index_min = i

a[index_min], a[index_max] = a[index_max], a[index_min]
print(' '.join([str(i) for i in a]))
