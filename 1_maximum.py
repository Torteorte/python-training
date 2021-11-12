n, m = [int(i) for i in input().split()]

a = [[int(j) for j in input().split()] for i in range(n)]

max_i = 0
max_j = 0
max_number = a[0][0]

for i in range(n):
    for j in range(m):
        if max_number < a[i][j]:
            max_i = i
            max_j = j
            max_number = a[i][j]

print(max_i, max_j)
