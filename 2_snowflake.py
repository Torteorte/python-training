n = int(input())

a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i] = ['.'] * n
    a[i][i] = '*'
    a[i][-i - 1] = '*'
    a[n // 2][i] = '*'
    a[n // 2][-i - 1] = '*'
    a[i][n // 2] = '*'

for snow_item in a:
    print(' '.join(snow_item))
