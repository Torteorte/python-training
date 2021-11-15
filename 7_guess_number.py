n = int(input())
possible_array = range(1, n + 1)

result_set = set(possible_array)

while True:
    data = input()
    if data == 'HELP':
        break
    answer_numbers = {int(x) for x in data.split()}
    answer = input()
    if answer == 'YES':
        result_set.intersection_update(answer_numbers)
    else:
        result_set.difference_update(answer_numbers)
print(result_set)
