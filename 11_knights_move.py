cell1 = int(input())
column1 = int(input())
cell2 = int(input())
column2 = int(input())
x = abs(cell1 - cell2)
y = abs(column1 - column2)

if x == 1 and y == 2 or y == 1 and x == 2 :
    print('YES')
else:
    print('NO')