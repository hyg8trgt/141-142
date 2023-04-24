from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(bright_stars_url)
soup = bs(page.text,'html.parser') 
star_table = soup.find_all('table')

# print(star_table)
temp_list=[]
table_rows= star_table[7].find_all('tr')

for tr in table_rows:
    td=tr.find_all("td")
    # print(td)
    row=[i.text.rstrip() for i in td ]
    # print(row)
    temp_list.append(row)

    
Star_Name = []
Distance = []
Mass=[]
Radius=[]

Luminosity=[]

for i in range(1,len(temp_list)):
    # print(temp_list [i])
    Star_Name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
my_data = pd.DataFrame(list(zip(Star_Name, Distance, Mass, Radius, )),columns=["star_name","Distance", "Mass","Radius",])
print(my_data )
my_data.to_csv("browndwarf.csv")

