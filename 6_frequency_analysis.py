import collections

strings = int(input())
counter = {}

for i in range(strings):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

pairs = [(-pair[1], pair[0]) for pair in collections.Counter(counter).most_common()]
words = [pair[1] for pair in sorted(pairs)]
print(words)
