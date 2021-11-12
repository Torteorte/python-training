number_max = 0
count_max = 0
number = int(input())
count = -1

while number != 0:
    if number_max < number:
        number_max = number
        count_max = count + 1
    number = int(input())
    count += 1
print(count_max)
