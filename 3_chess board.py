cell1 = int(input())
column1 = int(input())
cell2 = int(input())
column2 = int(input())

if (cell1 + column1 + cell2 + column2) % 2 == 0:
    print('YES')
else:
    print('NO')