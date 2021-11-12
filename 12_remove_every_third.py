string = input()

result_string = ''

for i in range(len(string)):
    if i % 3 != 0:
        result_string += string[i]
print(result_string)
