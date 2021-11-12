previous = 0
number = int(input())
count = -1

while number != 0:
    if number > previous:
        count += 1
    previous = number
    number = int(input())
print(count)
