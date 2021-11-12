array = input().split()

k, c = [int(s) for s in input().split()]
a = [int(s) for s in array]

a.insert(k, c)

print(a)
