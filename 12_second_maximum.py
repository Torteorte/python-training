n = int(input())
first_maximum = 0
second_maximum = 0

while n != 0:
    if n > first_maximum:
        second_maximum = first_maximum
        first_maximum = n
    if first_maximum > n > second_maximum:
        second_maximum = n
    n = int(input())
print(second_maximum)
