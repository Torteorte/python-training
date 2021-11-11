p = int(input())
x = int(input())
y = int(input())

deposit = x * 100 + y
result = deposit * (p / 100) + deposit

print(int(result // 100), int(result % 100))