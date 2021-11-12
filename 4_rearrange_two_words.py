string = input()
first = string[:string.find(' ')]
last = string[string.find(' ') + 1:]

print(last + ' ' + first)
