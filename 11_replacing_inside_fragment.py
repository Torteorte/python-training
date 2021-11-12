string = input()

a = string[:string.find('h') + 1]
b = string[string.find('h') + 1:string.rfind('h')]
c = string[string.rfind('h'):]
result = a + b.replace('h', 'H') + c

print(result)
