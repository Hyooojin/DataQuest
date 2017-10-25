from operator import itemgetter

total = 0
crime_rates = list()
with open('crime_rates.csv', 'r') as f:
    for line in f:
        city, rate = line.rstrip().split(',')
        crime_rates.append((city, int(rate)))
        total += int(rate)

hi_city, hi_rate = max(crime_rates, key=itemgetter(1))
lo_city, lo_rate = min(crime_rates, key=itemgetter(1))
avg_rate = total / len(crime_rates)

print('''\
Highest: {} - {} / 100,000 people
Lowest:  {} - {} / 100,000 people

Average crime rate of {} given cities is {:.2f} per 100,000
'''.format(hi_city, hi_rate, lo_city, lo_rate, len(crime_rates), avg_rate))
