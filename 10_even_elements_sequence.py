number = int(input())
count = 0

while number != 0:
    if number % 2 == 0:
        count += 1
    number = int(input())
print(count)
