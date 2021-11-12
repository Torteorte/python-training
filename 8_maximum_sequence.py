result = 0
number = int(input())

while number != 0:
    if result < number:
        result = number
    number = int(input())

print(result)
