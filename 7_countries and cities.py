countries = int(input())
obj = {}

for i in range(countries):
    country, *cities = input().split()
    obj[country] = cities

for i in range(int(input())):
    city = input()
    for country in obj:
        if city in obj[country]:
            print(country)
