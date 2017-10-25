from bs4 import BeautifulSoup
from re import findall


def scraper(filename):
    with open(filename, 'r') as f:
        soup = BeautifulSoup(f)
    return findall(r"'(.*?)'", soup.text)


def make_csv(filename, lst):
    with open(filename, 'w') as f:
        [f.write(a + '\n') for a in lst]

make_csv('spell_final_test.txt', scraper('test.html'))


# # enter below to grab it as a list
# weather_data = []
#
# with open('la_weather.csv', 'r') as f:
#     for line in f:
#         weather_data.append(line.rstrip())
# print(weather_data)
