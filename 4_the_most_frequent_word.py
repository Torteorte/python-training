strings = int(input())
counter = {}

for i in range(strings):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())

for key in sorted(counter):
    if counter[key] == max_count:
        print(key)
        break
