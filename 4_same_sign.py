array = input().split()

a = [int(i) for i in array]

for i in range(0, len(a)):
    if i != 0:
        if (a[i] > 0 and a[i - 1] > 0) or (a[i] < 0 and a[i - 1] < 0):
            print(a[i - 1], a[i])
            break
