cell1 = int(input())
column1 = int(input())
cell2 = int(input())
column2 = int(input())

if abs(cell1 - cell2) == abs(column1 - column2) or (cell1 == cell2) or (column1 == column2):
    print('YES')
else:
    print('NO')