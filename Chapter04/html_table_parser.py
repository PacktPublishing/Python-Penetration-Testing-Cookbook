import urllib2
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/html/html_tables.asp"
try:
    page = urllib2.urlopen(url)
except Exception as e:
    print e
    pass
soup = BeautifulSoup(page, "html.parser")

table = soup.find_all('table')[0]

new_table = pd.DataFrame(
    columns=['Company', 'Contact', 'Country'],
    index=range(0, 7))

row_number = 0
for row in table.find_all('tr'):
    column_number = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_number, column_number] = column.get_text()
        column_number += 1
    row_number += 1

print new_table
# Uncomment the bellow line to export to csv
# new_table.to_csv('table.csv')
# Uncomment the bellow line to export to excel
# new_table.to_excel('table.xlsx')
