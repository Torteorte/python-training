f_index = int(input())

a = 0
b = 1
c = 0
count = 0

if f_index == 1:
    c = 1
elif f_index != 0:
    while count != f_index - 1:
        c = a + b
        a = b
        b = c
        count += 1
print(c)
