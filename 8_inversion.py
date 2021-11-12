string = input()

a = string[:string.find('h')] 
b = string[string.find('h'):string.rfind('h') + 1]
c = string[string.rfind('h') + 1:]
result = a + b[::-1] + c

print(result)
