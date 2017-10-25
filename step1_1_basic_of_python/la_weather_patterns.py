from operator import itemgetter

with open('la_weather.csv', 'r') as f:
    # weather_data = [row.rstrip().split(',') for row in f]
    weather_column = [row.rstrip().split(',')[1] for row in f][1:]

# weather_counts = {a: weather_column.count(a) for a in set(weather_column)}
# print(weather_counts)

weather_cnt = tuple((a, weather_column.count(a)) for a in set(weather_column))

print(min(weather_cnt, key=itemgetter(1)))
print(max(weather_cnt, key=itemgetter(1)))
