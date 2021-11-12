array = input().split()

a = [int(i) for i in array]

for i in range(0, len(a)):
    for j in range(0, len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i])
