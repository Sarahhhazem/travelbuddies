# -*- coding: utf-8 -*-
"""Data_Scraping (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h4hZrIMvfaLXiO9fdUBBw0IjLBBOS7z5
"""

import pandas as pd
import numpy as np 
import json
import requests
from bs4 import BeautifulSoup

cities_list = ['Adelaide', 'Amsterdam', 'Athens', 'Auckland', 'Austin',
       'Buangkok', 'Barcelona', 'Beijing', 'Berlin', 'Bordeaux',
       'Boston', 'Brisbane', 'Brussels', 'Budapest', 'Buenos Aires', 'Cairns',
       'Canberra', 'Cancún', 'Cape Town', 'Cardiff',
       'Casablanca','Chicago', 'Copenhagen', 'Dubai', 'Dublin',
        'Edinburgh', 'Frankfurt', 'Galway', 
       'Halifax', 'Hong Kong', 'Honolulu', 'Istanbul', 'Jakarta',
       'Johannesburg', 'Kolkata', 'Kraków',
       'Kuala Lumpur', 'Las Vegas', 'Lima', 'Lisbon', 'London',
       'Los Angeles', 'Madrid', 'Manila', 'Marrakech', 'Melbourne',
       'Mexico City', 'Milan', 'Montreal', 'Moscow', 'Mostar',
       'Munich', 'Nashville', 'New Dehli', 'New York City',
       'Orlando', 'Ottawa', 'Paris', 'Perth', 'Prague', 'Quebec', 'Reykjavik',
       'Riga', 'Rio De Janeiro', 'Rome', 'San Francisco', 'Santiago',
       'Sao Paulo', 'Savannah', 'Seattle', 'Seoul', 
       'Singapore', 'St. Petersburg', 'Stockholm', 'Sydney', 'Taipei',
       'Tallinn', 'Tokyo', 'Toronto', 'Valletta', 'Vancouver', 'Vienna',
       'Washington D.C.', 'Wellington', 'Marseille', 'Belfast','Antwerp',
       'Calgary', 'Helsinki','Lyon', 'Oslo', 'Warsaw', 'Zurich', 'Brighton',
       'Bristol', 'Glasgow', 'Leeds', 'Liverpool' , 'Manchester', 'San Diego',
       'Santa Barbara', 'Baltimore', 'Philadelphia', ]

cities_urls= [
"https://www.tripadvisor.com/Attractions-g255093-Activities-Adelaide_Greater_Adelaide_South_Australia.html",
"https://www.tripadvisor.com/Attractions-g188590-Activities-Amsterdam_North_Holland_Province.html",
"https://www.tripadvisor.com/Attractions-g189400-Activities-Athens_Attica.html" ,
"https://www.tripadvisor.com/Attractions-g1811027-Activities-Auckland_North_Island.html" ,
"https://www.tripadvisor.com/Attractions-g30196-Activities-Austin_Texas.html" ,
"https://www.tripadvisor.com/Attractions-g293916-Activities-Bangkok.html" ,
"https://www.tripadvisor.com/Attractions-g187497-Activities-Barcelona_Catalonia.html" ,
"https://www.tripadvisor.com/Attractions-g294212-Activities-Beijing.html" ,
"https://www.tripadvisor.com/Attractions-g187323-Activities-Berlin.html" ,
"https://www.tripadvisor.com/Attractions-g187079-Activities-Bordeaux_Gironde_Nouvelle_Aquitaine.html" ,
"https://www.tripadvisor.com/Attractions-g60745-Activities-Boston_Massachusetts.html" ,
"https://www.tripadvisor.com/Attractions-g255068-Activities-Brisbane_Brisbane_Region_Queensland.html" ,
"https://www.tripadvisor.com/Attractions-g188644-Activities-Brussels.html",
"https://www.tripadvisor.com/Attractions-g274887-Activities-Budapest_Central_Hungary.html",
"https://www.tripadvisor.com/Attractions-g312741-Activities-Buenos_Aires_Capital_Federal_District.html",
"https://www.tripadvisor.com/Attractions-g255069-Activities-Cairns_Cairns_Region_Queensland.html",
"https://www.tripadvisor.com/Attractions-g255057-Activities-Canberra_Australian_Capital_Territory.html",
"https://www.tripadvisor.com/Attractions-g150807-Activities-Cancun_Yucatan_Peninsula.html",
"https://www.tripadvisor.com/Attractions-g1722390-Activities-Cape_Town_Western_Cape.html",
"https://www.tripadvisor.com/Attractions-g186460-Activities-Cardiff_South_Wales_Wales.html",
"https://www.tripadvisor.com/Attractions-g293732-Activities-Casablanca_Grand_Casablanca_Region.html",
"https://www.tripadvisor.com/Attractions-g35805-Activities-Chicago_Illinois.html",
"https://www.tripadvisor.com/Attractions-g189541-Activities-Copenhagen_Zealand.html",
"https://www.tripadvisor.com/Attractions-g295424-Activities-Dubai_Emirate_of_Dubai.html",
"https://www.tripadvisor.com/Attractions-g186605-Activities-Dublin_County_Dublin.html",
"https://www.tripadvisor.com/Attractions-g186525-Activities-Edinburgh_Scotland.html",
"https://www.tripadvisor.com/Attractions-g187337-Activities-Frankfurt_Hesse.html",
"https://www.tripadvisor.com/Attractions-g186609-Activities-Galway_County_Galway_Western_Ireland.html",
"https://www.tripadvisor.com/Attractions-g154976-Activities-Halifax_Halifax_Regional_Municipality_Nova_Scotia.html",
"https://www.tripadvisor.com/Attractions-g294217-Activities-Hong_Kong.html",
"https://www.tripadvisor.com/Attractions-g60982-Activities-Honolulu_Oahu_Hawaii.html",
"https://www.tripadvisor.com/Attractions-g293974-Activities-Istanbul.html",
"https://www.tripadvisor.com/Attractions-g294229-Activities-Jakarta_Java.html",
"https://www.tripadvisor.com/Attractions-g312578-Activities-Johannesburg_Greater_Johannesburg_Gauteng.html",
"https://www.tripadvisor.com/Attractions-g304558-Activities-Kolkata_Calcutta_Kolkata_District_West_Bengal.html",
"https://www.tripadvisor.com/Attractions-g274772-Activities-Krakow_Lesser_Poland_Province_Southern_Poland.html",
"https://www.tripadvisor.com/Attractions-g298570-Activities-Kuala_Lumpur_Wilayah_Persekutuan.html",
"https://www.tripadvisor.com/Attractions-g45963-Activities-Las_Vegas_Nevada.html",
"https://www.tripadvisor.com/Attractions-g294316-Activities-Lima_Lima_Region.html",
"https://www.tripadvisor.com/Attractions-g189158-Activities-Lisbon_Lisbon_District_Central_Portugal.html",
"https://www.tripadvisor.com/Attractions-g186338-Activities-London_England.html",
"https://www.tripadvisor.com/Attractions-g32655-Activities-Los_Angeles_California.html",
"https://www.tripadvisor.com/Attractions-g187514-Activities-Madrid.html",
"https://www.tripadvisor.com/Attractions-g298573-Activities-Manila_Metro_Manila_Luzon.html",
"https://www.tripadvisor.com/Attractions-g293734-Activities-Marrakech_Marrakech_Tensift_El_Haouz_Region.html",
"https://www.tripadvisor.com/Attractions-g255100-Activities-Melbourne_Victoria.html",
"https://www.tripadvisor.com/Attractions-g150800-Activities-Mexico_City_Central_Mexico_and_Gulf_Coast.html",
"https://www.tripadvisor.com/Attractions-g187849-Activities-Milan_Lombardy.html",
"https://www.tripadvisor.com/Attractions-g155032-Activities-Montreal_Quebec.html",
"https://www.tripadvisor.com/Attractions-g298484-Activities-Moscow_Central_Russia.html",
"https://www.tripadvisor.com/Attractions-g295388-Activities-Mostar_Herzegovina_Neretva_Canton_Federation_of_Bosnia_and_Herzegovina.html",
"https://www.tripadvisor.com/Attractions-g187309-Activities-Munich_Upper_Bavaria_Bavaria.html",
"https://www.tripadvisor.com/Attractions-g55229-Activities-Nashville_Davidson_County_Tennessee.html",
"https://www.tripadvisor.com/Attractions-g304551-Activities-New_Delhi_National_Capital_Territory_of_Delhi.html",
"https://www.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html",
"https://www.tripadvisor.com/Attractions-g34515-Activities-Orlando_Florida.html",
"https://www.tripadvisor.com/Attractions-g155004-Activities-Ottawa_Ontario.html",
"https://www.tripadvisor.com/Attractions-g187147-Activities-Paris_Ile_de_France.html",
"https://www.tripadvisor.com/Attractions-g255103-Activities-Perth_Greater_Perth_Western_Australia.html",
"https://www.tripadvisor.com/Attractions-g274707-Activities-Prague_Bohemia.html",
"https://www.tripadvisor.com/Attractions-g155025-Activities-Quebec.html",
"https://www.tripadvisor.com/Attractions-g189970-Activities-Reykjavik_Capital_Region.html",
"https://www.tripadvisor.com/Attractions-g274967-Activities-Riga_Riga_Region.html",
"https://www.tripadvisor.com/Attractions-g303506-Activities-Rio_de_Janeiro_State_of_Rio_de_Janeiro.html",
"https://www.tripadvisor.com/Attractions-g187791-Activities-Rome_Lazio.html",
"https://www.tripadvisor.com/Attractions-g60713-Activities-San_Francisco_California.html",
"https://www.tripadvisor.com/Attractions-g294305-Activities-Santiago_Santiago_Metropolitan_Region.html",
"https://www.tripadvisor.com/Attractions-g303631-Activities-Sao_Paulo_State_of_Sao_Paulo.html",
"https://www.tripadvisor.com/Attractions-g60814-Activities-Savannah_Georgia.html",
"https://www.tripadvisor.com/Attractions-g60878-Activities-Seattle_Washington.html",
"https://www.tripadvisor.com/Attractions-g294197-Activities-Seoul.html",
"https://www.tripadvisor.com/Attractions-g294265-Activities-Singapore.html",
"https://www.tripadvisor.com/Attractions-g298507-Activities-St_Petersburg_Northwestern_District.html",
"https://www.tripadvisor.com/Attractions-g189852-Activities-Stockholm.html",
"https://www.tripadvisor.com/Attractions-g255060-Activities-Sydney_New_South_Wales.html",
"https://www.tripadvisor.com/Attractions-g293913-Activities-Taipei.html",
"https://www.tripadvisor.com/Attractions-g274958-Activities-Tallinn_Harju_County.html",
"https://www.tripadvisor.com/Attractions-g298184-Activities-Tokyo_Tokyo_Prefecture_Kanto.html",
"https://www.tripadvisor.com/Attractions-g155019-Activities-Toronto_Ontario.html",
"https://www.tripadvisor.com/Attractions-g190328-Activities-Valletta_Island_of_Malta.html",
"https://www.tripadvisor.com/Attractions-g154943-Activities-Vancouver_British_Columbia.html",
"https://www.tripadvisor.com/Attractions-g190454-Activities-Vienna.html",
"https://www.tripadvisor.com/Attractions-g28970-Activities-Washington_DC_District_of_Columbia.html",
"https://www.tripadvisor.com/Attractions-g255115-Activities-Wellington_Greater_Wellington_North_Island.html",
"https://www.tripadvisor.com/Attractions-g187253-Activities-Marseille_Bouches_du_Rhone_Provence_Alpes_Cote_d_Azur.html ", 
"https://www.tripadvisor.com/Attractions-g186470-Activities-Belfast_Northern_Ireland.html",
"https://www.tripadvisor.com/Attractions-g188636-Activities-Antwerp_Antwerp_Province.html",
"https://www.tripadvisor.com/Attractions-g154913-Activities-Calgary_Alberta.html",
"https://www.tripadvisor.com/Attractions-g189934-Activities-Helsinki_Uusimaa.html",
"https://www.tripadvisor.com/Attractions-g187265-Activities-Lyon_Rhone_Auvergne_Rhone_Alpes.html",
"https://www.tripadvisor.com/Attractions-g190479-Activities-Oslo_Eastern_Norway.html",
"https://www.tripadvisor.com/Attractions-g274856-Activities-Warsaw_Mazovia_Province_Central_Poland.html",
"https://www.tripadvisor.com/Attractions-g188113-Activities-Zurich.html",
"https://www.tripadvisor.com/Attractions-g186273-Activities-Brighton_East_Sussex_England.html",
"https://www.tripadvisor.com/Attractions-g186220-Activities-Bristol_England.html",
"https://www.tripadvisor.com/Attractions-g186534-Activities-Glasgow_Scotland.html",
"https://www.tripadvisor.com/Attractions-g186411-Activities-Leeds_West_Yorkshire_England.html",
"https://www.tripadvisor.com/Attractions-g186337-Activities-Liverpool_Merseyside_England.html",
"https://www.tripadvisor.com/Attractions-g187069-Activities-Manchester_Greater_Manchester_England.html",
"https://www.tripadvisor.com/Attractions-g60750-Activities-San_Diego_California.html",
"https://www.tripadvisor.com/Attractions-g33045-Activities-Santa_Barbara_California.html",
"https://www.tripadvisor.com/Attractions-g60811-Activities-Baltimore_Maryland.html",
"https://www.tripadvisor.com/Attractions-g60795-Activities-Philadelphia_Pennsylvania.html",]

def get_att(url):
    try:
      import requests
      from bs4 import BeautifulSoup 
      import pandas as pd
      import numpy as np 
      import re

      response = requests.get(url)
      results_page =  BeautifulSoup(response.content, 'lxml')
      links = results_page.find_all('a', {"class":"ui_tab attractions-attractions-category-bar-AttractionsMenuTab__menuTab--TonFq"})
      attractions_urls = []
      for i in range(len(links)):
        a_url=url + links[i].get('href')
        attractions_urls.append(a_url)

      response = requests.get(attractions_urls[0])
      results = BeautifulSoup(response.content, 'lxml')
      names = results.find_all('span', {"class":"common-filters-LinkableFilterLabel__labelWrapper--1X145"})
      counts = results.find_all('span', {"class": "common-filters-LinkableFilterLabel__count--fSpDk"})

      attr_arr = []
      count_arr = []
      tour_arr=[]
      link_arr=[]
      tour_count_arr=[]
      attr=' '

      for i in range(len(names)):
        attr = names[i].get_text()
        count = counts[i].get_text()
        tour_arr = np.append(tour_arr, attr)
        tour_count_arr = np.append(tour_count_arr, count)


      for t in range(len(tour_arr)):
        if tour_arr[t][0]=='$':
          break 
        attr_arr = np.append(attr_arr, tour_arr[t])
        count_arr = np.append(count_arr, tour_count_arr[t])
        link_arr = np.append(link_arr,attractions_urls[0])

        for l in range(len(attractions_urls)-1):
          response = requests.get(attractions_urls[l+1])
          results = BeautifulSoup(response.content, 'lxml')
          names = results.find_all('span', {"class":"common-filters-LinkableFilterLabel__labelWrapper--1X145"})
          attrs = results.find_all('a', {"class": "taLnk"})

          attrs_text=[]

          for i in range(len(attrs)):
            attr=attrs[i].get_text()
            if attr[-1]==')':
              attr_s = attr.split('(')
              name = attr_s[0][:-1]
              count = int(attr_s[1][:-1])
              attr_arr = np.append(attr_arr, name)
              count_arr = np.append(count_arr, count)
              link_arr = np.append(link_arr,attractions_urls[l+1])

      df_c = pd.DataFrame()
      df_c['attribute'] = attr_arr
      df_c['count'] = count_arr.astype('int32')

      df_l = pd.DataFrame()
      df_l['attribute'] = attr_arr
      df_l['link'] = link_arr

      return df_c,df_l

    except Exception as e:
      print("Error: ", e)
      df = pd.DataFrame()
      return df, df

def get_all(i):
    print(cities_list[i])
    df_c,df_l=get_att(cities_urls[i])

    city_df = df_c.rename(columns={"count": cities_list[i]}).transpose()
    city_df.columns = city_df.iloc[0]
    city_df=city_df.drop(['attribute'])

    links_df = df_l.rename(columns={"link": cities_list[i]}).transpose()
    links_df.columns = links_df.iloc[0]
    links_df=links_df.drop(['attribute'])

    return city_df, links_df

##Combining Data

x = []
#for i in range(len(cities_list)):
for i in range(4):
    try:
        getall = get_all(i)[0].T.to_dict()
        x.append(getall)
    except Exception as e :
        print("Error 6:", e)
        
y = []
#for i in range(len(cities_list)):
for i in range(4):
    try:
        getall = get_all(i)[1].T.to_dict()
        y.append(getall)
    except Exception as e :
        print("Error 6:", e)

a = {}
for i in x:
  a = {**a, **i}

cities_df = pd.DataFrame(a)
cities_df = cities_df.fillna(0).T
cities_df = cities_df.reset_index().rename(columns ={'index': 'City'})
cities_df = cities_df.set_index('City')

b = {}
for i in y:
  b = {**b, **i}

links_df = pd.DataFrame(b)
links_df = links_df.fillna(0).T
links_df = links_df.reset_index().rename(columns ={'index': 'City'})
links_df = links_df.set_index('City')

links_df.to_csv('links_df.csv')

url = "http://www.worldcitiescultureforum.com/data"
response = requests.get(url)
results_page = BeautifulSoup(response.content, 'lxml')
indicators = results_page.find_all('div',{"class":'col data-first'})

#returns indicator df for each indicator in page one 
def get_df_page_one(n):
  import requests
  from bs4 import BeautifulSoup 
  link = "http://www.worldcitiescultureforum.com/" + indicators[n].find('a').get('href')
  response = requests.get(link)
  indicator =  BeautifulSoup(response.content, 'lxml')
  name = indicator.find('title').get_text()
  indicator_csv = indicator.find('a', {"class":"box col-1 align-right no-mobile"}).get('href')
  datasource = indicator_csv
  df = pd.read_csv(datasource,sep=",",error_bad_lines=False)
  df = df.drop(['Per capita', 'Date','Source', 'Notes'], axis = 1)
  df = df.dropna()
  grp = df.groupby(['City']).first()
  out = grp.apply(pd.Series)
  out = out.rename(columns={"Figure": name})
  return  out

url2 = results_page.find('div',{"class":"side right"}).find('a').get('href')
response2= requests.get(url2)
results_page2 = BeautifulSoup(response2.content, 'lxml')
indicators2 = results_page2.find_all('div',{"class":'col data-first'})

#returns indicator df for each indicator in page two 
def get_df_page_two(n):
  import requests
  from bs4 import BeautifulSoup 
  link = "http://www.worldcitiescultureforum.com/" + indicators2[n].find('a').get('href')
  response = requests.get(link)
  indicator =  BeautifulSoup(response.content, 'lxml')
  name = indicator.find('title').get_text()
  indicator_csv = indicator.find('a', {"class":"box col-1 align-right no-mobile"}).get('href')
  datasource = indicator_csv
  df = pd.read_csv(datasource,sep=",",error_bad_lines=False)
  df = df.drop(['Per capita', 'Date','Source', 'Notes'], axis = 1)
  grp = df.groupby(['City']).first()
  out = grp.apply(pd.Series)
  out = out.rename(columns={"Figure": name})
  return out

dfs = []
for i in range(1,40):
  a = get_df_page_one(i)
  dfs.append(a)
for x in range(1,13):
  b = get_df_page_two(x)
  dfs.append(b)
for y in range(15,19):
  c = get_df_page_two(y)
  dfs.append(c)
m = get_df_page_two(20)
w = get_df_page_two(24)
dfs.append(m)
dfs.append(w)
dataf = pd.concat(dfs, axis=1, join='outer', ignore_index=False, sort = True)

def convert_to_float(number):
    try:
        return float(number.strip('$').strip(' ').replace(",", ''))
    except:
        return number

def convert_p_to_float(number):
    try:
        return float(number.strip(' ').replace(",", '').strip('%'))/100
    except:
        return np.nan      

for i in range(len(dataf.columns)):
  try:
    if dataf[dataf.columns[i]][31][-1]!="%":
      dataf[dataf.columns[i]]=dataf[dataf.columns[i]].apply(convert_to_float).astype(float)
    else: 
      dataf[dataf.columns[i]]=dataf[dataf.columns[i]].apply(convert_p_to_float).astype(float)
  except:
    dataf[dataf.columns[i]]=dataf[dataf.columns[i]].apply(convert_to_float).astype(float)

#data from second dataset 
datasource = 'https://data.london.gov.uk/download/global-city-data/ffcefcba-829c-4220-911f-d4bf17ef75d6/global-city-indicators.xlsx'
df=pd.read_excel(datasource,sheet_name="World Cities data",index_col=0,)
df=df.drop('London Data Source',axis=1).transpose()
df=df[df.columns[df.columns.notnull()]]
df=df[df.columns[:45]]
df=df[df.columns[df.iloc[0,:]!=df.index[0]]]
df.index=df.index.rename("City")
df=df.replace("-----",np.nan)
df=df.replace("Yes",'1')
df=df=df.replace("No",'0')

#dummy variables for public transportation methods
df = df.merge(df['Public Transportation'].str.get_dummies(sep=','), left_on="City",right_on="City")


#i dropped these columns because they were giving me so much trouble when converting to floats 
df.drop(df[['Annual Population Growth',"Primary Industry","Secondary Industry",'Public Transportation','Metro Population (millions)','Share of Global 500 Companies (%)','City Population (millions)','Students Enrolled in Higher Education']],axis=1, inplace = True)

#convert to float
for i in range(len(df.columns)):
  try:
    df[df.columns[i]]=df[df.columns[i]].apply(convert_to_float).astype(float)
  except:
   i=i+1

import requests
from bs4 import BeautifulSoup 
link = "https://www.listchallenges.com/print-list/41692" 
response = requests.get(link)
indicator =  BeautifulSoup(response.content, 'lxml')
text = indicator.find('div', {"id":"repeaterItems"}).get_text()[6:-1]
cities_list = text.split('\r\n\t\t\t\r\n\t\t\t\t')
for i in range(len(cities_list)):
  cities_list[i]=cities_list[i].replace(',','.').split('. ')
cities_list[17]=['18', 'Cairns', 'Australia']
cities_list[87]=['88', 'St. Petersburg', 'Russia']
cities=pd.DataFrame(cities_list)
cities.drop(cities.columns[[0,3]],axis=1, inplace = True)
cities.columns= ['City','Country']
cities.set_index('City')
cities.info()

#merge first dataset with list of cities as main sataset
final_table =cities.join(dataf, on='City')
#merge second dataset with main dataset
final_table_exp=final_table.join(df,on='City')
final_table_exp=final_table_exp.set_index("City")

### final Cities Dataset 
final_table_exp2=cities_df.join(final_table_exp,on='City')
final_table_exp2=final_table_exp2.drop("Country", axis=1)
final_table_exp2 = final_table_exp2.fillna(0)
final_table_exp2 = final_table_exp2.reset_index().rename(columns ={'index': 'City'})

final_table_exp2.to_csv('final_table_exp2.csv')

with open('/Users/pasbell/Google Drive/College/4th Year/Fall/Data Analytics/Class Notebooks/yelp_credentials.txt','r') as f:
    count = 0
    for line in f:
        if count == 0:
            CLIENT_ID = line.strip()
        if count == 1:
            API_KEY = line.strip()
        count+=1

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com' #The API url header
SEARCH_PATH = '/v3/businesses/search' #The path for an API request to find businesses
BUSINESS_PATH = '/v3/businesses/'  # The path to get data for a single business

#This function gets the list of businesses near the location
def get_restaurants(api_key,location,number):
    try:
        import requests

        offset = 0
        businesses = []
        #First we get the access token
        #Set up the search data dictionary
        search_data = {
        'term': "restaurant",
        'location': location.replace(' ', '+'),
        'limit': 50,
        'offset' : offset
        }
        url = API_HOST + SEARCH_PATH
        headers = {
            'Authorization': 'Bearer %s' % api_key,
        }

        if number < 50:
            offset_limit = 0
        else:
            offset_limit = number - 50

        while offset <= offset_limit:
            response = requests.request('GET', url, headers=headers, params=search_data).json()

            results = response.get('businesses')
            businesses.extend(results)

            offset+=50
            search_data['offset'] = offset

        return businesses[:number]
    except Exception as e:
        print("Error 1:", e)
        return list()
        

#This function gets reviews for each business from yelp
def get_business_review(api_key,business_id):
    import json
    import requests
    
    try:
        business_path = BUSINESS_PATH + business_id+"/reviews"
        url = API_HOST + business_path

        headers = {
            'Authorization': 'Bearer %s' % api_key,
        }


        response = requests.request('GET', url, headers=headers).json()

        review_text = ''
        for review in response['reviews']:
            review_text += review['text']
        return review_text
    except Exception as e:
        print("Error 2:", e)
        return ''


#This function gets restaurants (businesses) and then reviews for each restaurant
def get_reviews(location, number):
    try:
        restaurants = get_restaurants(API_KEY,location, number)

        if not restaurants:
            return None
        restaurant_details = list()
        review_list = list()
        for restaurant in restaurants:
            restaurant_name = restaurant['name']
            restaurant_rating = restaurant['rating']
            restaurant_categories = restaurant['categories']
            restaurant_city = restaurant['location']['city']
            restaurant_location = restaurant['coordinates']
            restaurant_id = restaurant['id']

            review_reviews = get_business_review(API_KEY,restaurant_id)
            restaurant_details.append((restaurant_name,restaurant_rating,restaurant_categories, restaurant_city, restaurant_location ))
            review_list.append((restaurant_name, review_reviews))
        return restaurant_details, review_list
    except Exception as e:
        print("Error 3:", e)
        return [], []

def get_nrc_data():
    nrc = "/Users/pasbell/Google Drive/College/4th Year/Fall/Data Analytics/Class Notebooks/local_nltk_data/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt"
    count=0
    emotion_dict=dict()
    with open(nrc,'r') as f:
        all_lines = list()
        for line in f:
            if count < 46:
                count+=1
                continue
            line = line.strip().split('\t')
            if int(line[2]) == 1:
                if emotion_dict.get(line[0]):
                    emotion_dict[line[0]].append(line[1])
                else:
                    emotion_dict[line[0]] = [line[1]]
    return emotion_dict   

emotion_dict = get_nrc_data()

def emotion_analyzer(text,emotion_dict=emotion_dict):
    try:
        #Set up the result dictionary
        emotions = {x for y in emotion_dict.values() for x in y}
        emotion_count = dict()
        for emotion in emotions:
            emotion_count[emotion] = 0

        #Analyze the text and normalize by total number of words
        total_words = len(text.split())
        for word in text.split():
            if emotion_dict.get(word):
                for emotion in emotion_dict.get(word):
                    emotion_count[emotion] += 1/len(text.split())
        return emotion_count
    except Exception as e:
        print("Error 4:", e)
        return dict()

def comparative_emotion_analyzer(doc_tuples):
    try:
        import pandas as pd
        df = pd.DataFrame(columns=['Name','Anger','Fear','Trust','Negative',
                               'Positive','Joy','Disgust','Anticipation',
                               'Sadness','Surprise'])
        df.set_index("Name",inplace=True)

        output = df    
        for text_tuple in doc_tuples:
            text = text_tuple[1] 
            result = emotion_analyzer(text)
            df.loc[text_tuple[0]] = [result['anger'],result['fear'],result['trust'],
                      result['negative'],result['positive'],result['joy'],result['disgust'],
                      result['anticipation'],result['sadness'],result['surprise']]
        return output
    except Exception as e:
        print("Error 5:", e)
        df = pd.DataFrame(columns=['Name','Anger','Fear','Trust','Negative',
                               'Positive','Joy','Disgust','Anticipation',
                               'Sadness','Surprise'])
        df.set_index("Name",inplace=True)
        return df

def get_restaurant_attributes(city):
    
    print(city)
    
    #API from Yelp
    restaurant_details, review_list = get_reviews(city, 50)
    
    ##Clean Data

    restaurants_df = pd.DataFrame(restaurant_details, columns = ['Name', 'Rating', 'Categories', 'City', 'Location'])
    restaurants_df.City = city
    restaurants_df['Latitude'] = restaurants_df['Location'].apply(lambda x: x['latitude'])
    restaurants_df['Longitude'] = restaurants_df['Location'].apply(lambda x: x['longitude'])
    restaurants_df=restaurants_df.drop(['Location'], axis=1)

    restaurants_df['Categories'] = restaurants_df['Categories'].apply(lambda x: [y['alias'] for y in x])
    restaurants_df = restaurants_df.set_index('Name')


    ##Convert Categories to columns
    restaurants_df['Categories'] = restaurants_df['Categories'].apply(lambda x: ','.join(x))
    restaurants_df = restaurants_df.merge(restaurants_df['Categories'].str.get_dummies(sep=','), left_on="Name",right_on="Name")
    restaurants_df=restaurants_df.drop(['Categories'], axis=1)
    cols = list(restaurants_df.columns)
    cols =  cols[1:] + [cols[0]]
    restaurants_df = restaurants_df[cols]
    restaurants_df = restaurants_df.reset_index()

    #Add Review Emotions
    restaurants_df = restaurants_df.merge(comparative_emotion_analyzer(review_list), left_on="Name",right_on="Name")
    restaurants_df = restaurants_df.set_index('Name')

    return restaurants_df

x = []
for i in cities_list:
    try:
        getattributes = get_restaurant_attributes(i).T.to_dict()
        x.append(getattributes)
    except Exception as e :
        print("Error 6:", e)
    

a = {}

for i in x:
    a.update(i)

all_restaurants = pd.DataFrame(a).fillna(0).T
all_restaurants = all_restaurants.reset_index().rename(columns={'index':"Name"})

pd.DataFrame(all_restaurants.columns).to_csv('rest_atts')

def recommend_restaurants(city, number_rests, rest_names):
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import NearestNeighbors
    import numpy as np
    
    for rest_name in rest_names:
        new_rest = get_restaurant_attributes('New York', rest_name)
        new_rest.rename(index={0:all_restaurants.shape[0]},inplace=True)
        all_restaurants = all_restaurants.append(new_rest)
        
    all_restaurants = all_restaurants.fillna(0)

    restaurant_indices = np.arange(all_restaurants.shape[0]-(len(rest_names)-1)-1, all_restaurants.shape[0])
    print(restaurant_indices)
    
    not_features = ['City', 'Name', 'Latitude', 'Longitude']
    rest_cols = all_restaurants.columns.values
    city_index = np.where(rest_cols=='City')[0][0]
    name_index = np.where(rest_cols=='Name')[0][0]
    latitude_index = np.where(rest_cols=='Latitude')[0][0]
    longitude_index = np.where(rest_cols=='Longitude')[0][0]

    not_feature_indices = [city_index, name_index, latitude_index, longitude_index]
    features = np.delete(all_restaurants.columns.values, not_feature_indices)

    scaler = StandardScaler()
    scaler.fit(all_restaurants.loc[:, features])
    restaurants = scaler.transform(all_restaurants.loc[:, features])

    N = all_restaurants.shape[0]
    model = NearestNeighbors(n_neighbors=N)
    model.fit(restaurants)
    distances, indices = model.radius_neighbors(restaurants[restaurant_indices, :], radius=np.inf)
    distance = np.sum(distances)
    indices_reordered = np.argsort(distance)

    rest_recs = all_restaurants.loc[indices_reordered, not_features].drop(restaurant_indices)
    return rest_recs[rest_recs["City"]==city]['Name'].values[0:number_rests]

x = []
for i in cities_list:
    try:
        getattributes = get_restaurant_attributes(i).T.to_dict()
        x.append(getattributes)
    except Exception as e :
        print("Error 6:", e)
    

a = {}

for i in x:
    a.update(i)

all_restaurants = pd.DataFrame(a).fillna(0).T
all_restaurants = all_restaurants.reset_index().rename(columns={'index':"Name"})

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:123Pl,Okm@localhost/Travel_Buddy"
                       .format(user="root",
                               pw="123Pl,Okm",
                               db="travels"))

all_restaurants.to_sql('all_restaurants', con = engine, if_exists='replace', index_label='id');