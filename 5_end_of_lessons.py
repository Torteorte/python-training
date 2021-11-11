lesson = int(input())
result = lesson * 45 + (lesson // 2) * 5 + ((lesson + 1) // 2 - 1) * 15

print(result // 60 + 9, result % 60)