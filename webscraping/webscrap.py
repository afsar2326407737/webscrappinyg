import requests
from bs4 import BeautifulSoup as bs

import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response = requests.get(url)
print(response)

htmlcontent=response.content
soup = bs(htmlcontent, 'html.parser')

title = soup.find('title')
print(title.getText())
population_table = soup.find('tbody')

country_names = []

for row in population_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) > 1:
        country_name = cells[1].get_text(strip=True)
        country_names.append(country_name)




population_number = []
for i in population_table.findAll('tr'):
    cells = i.findAll('td')
    if len(cells) > 1:
        population = cells[2].get_text(strip=True)
        population_number.append(population)

percentage = []

for i in population_table.findAll('tr'):
    cells = i.findAll('td')
    if len(cells) > 1:
        percentage_ = cells[3].get_text(strip=True)
        percentage.append(percentage_)


data = {
    'Country': country_names,
    'Population': population_number,
    'Percentage': percentage
}

print(data)

import pandas as pd
df = pd.DataFrame(data)
df.to_excel('web.xlsx' , index = False)
