string = input()

first = string.find('f')
last = string.rfind('f')

if first != -1:
    if first == last:
        print(first)
    else:
        print(first, last)
