string = input()

first_word = string.find('h')
last_word = string.rfind('h')

print(string[0:first_word] + string[last_word + 1:])
