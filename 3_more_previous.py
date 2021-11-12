array = input().split()

for i in range(0, len(array)):
    if i != 0 and array[i] > array[i - 1]:
        print(array[i])
