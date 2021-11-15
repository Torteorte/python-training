files = int(input())

available_actions = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_data = {}

for i in range(files):
    file, *access = input().split()
    file_data[file] = access
print(file_data)

actions_with_file = int(input())

for i in range(actions_with_file):
    action, file = input().split()
    if available_actions[action] in file_data[file]:
        print('OK')
    else:
        print('Access denied')
