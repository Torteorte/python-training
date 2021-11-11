deg = float(input())

h = int(deg // 30)
m = int(deg % 30 * 2)
s = int(deg % 0.5 * 120)

print(h, m, s)