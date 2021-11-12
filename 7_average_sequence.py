result = 0
number = int(input())
count = 0

while number != 0:
    result += number
    number = int(input())
    count += 1
print(result / count)
