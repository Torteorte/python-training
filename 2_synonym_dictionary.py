words = int(input())
obj = {}

for i in range(words):
    first, second = input().split()
    obj[first] = second
    obj[second] = first

search_word = input()
print(obj[search_word])
