n = int(input())

two_power = 2
cont = 1

while two_power <= n:
    two_power *= 2
    cont += 1
print(cont - 1, two_power / 2)
