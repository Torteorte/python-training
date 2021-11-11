cell1 = int(input())
column1 = int(input())
cell2 = int(input())
column2 = int(input())

if abs(cell1 - cell2) <= 1 and abs(column1 - column2) <= 1:
    print('YES')
else:
    print('NO')