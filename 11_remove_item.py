array = input().split()
k = int(input())

a = [int(s) for s in array]

a.pop(k)

print(a)
