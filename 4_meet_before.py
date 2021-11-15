initial_array = input().split()
set_array = []

for i in initial_array:
    if i in set_array:
        print('YES')
    else:
        set_array.append(i)
        print('NO')
