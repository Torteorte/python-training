initial_obj = input().split()

counter = {}

for word in initial_obj:
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1)
