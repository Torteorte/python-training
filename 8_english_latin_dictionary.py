words = int(input())
dictionary = {}
latin_words = []

for i in range(words):
    english, _, *latin = input().replace(',', '').split()
    dictionary[english] = latin
    latin_words += dictionary[english]

for latin in sorted(set(latin_words)):
    for key in dictionary:
        if latin in dictionary[key]:
            print(latin + " - " + key)
