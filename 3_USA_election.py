candidates = int(input())
obj = {}

for i in range(candidates):
    candidate, votes = input().split()
    obj[candidate] = obj.get(candidate, 0) + int(votes)

for candidate, votes in sorted(obj.items()):
    print(candidate, votes)
