array = input().split()
x = int(input())

place = 0
a = [int(i) for i in array]

for i in range(0, len(a)):
    if x > a[i]:
        place = i + 1
        break
if place == 0:
    place = len(a) + 1

print(place)
