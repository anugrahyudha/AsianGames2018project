
# coding: utf-8

# In[1]:


# import libraries
import urllib.request # ada juga import urllib.error
from bs4 import BeautifulSoup

from requests import get #beda dengan urllib.request

import pandas as pd

import string
import re

import math


# In[2]:


from time import sleep
import time
from random import randint

from IPython.core.display import clear_output


# In[2]:


#Medallists page
all_url = 'https://en.asiangames2018.id/medals/winners/'
response = get(all_url)
medallists_soup = BeautifulSoup(response.text, 'html.parser')
table = medallists_soup.find_all('table')


# In[3]:


table


# In[4]:


medallists = medallists_soup.find_all('tr', class_ = 'or-e')


# In[5]:


print(len(medallists))


# In[36]:


records = []
for winner in medallists:
    rank = winner.find('span', class_ = 'orp-rk').text
    country = winner.find('img', class_ = 'or-fgs')['title']
    url = 'https://en.asiangames2018.id' + winner.find('a', class_ = 'or-js-w-lk')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya
    name = winner.find('span', class_ = 'or-name').text
    surname = winner.find('span', class_ = 'or-surname').text
    sport = winner.find('a', class_ = 'or-sport-name')['title']
    gold = winner.find('td', class_ = 'or-md or-gold').text
    silver = winner.find('td', class_ = 'or-md or-gold').text
    bronze = winner.find('td', class_ = 'or-md or-silver').text
    medals = winner.find('td', class_ = 'or-md or-total').text
    
    rank = rank.replace(' ', '')
    rank = rank.replace('\r\n', '')
    gold = gold.replace(' ', '')
    gold = gold.replace('\r\n', '')
    silver = silver.replace(' ', '')
    silver = silver.replace('\r\n', '')
    bronze = bronze.replace(' ', '')
    bronze = bronze.replace('\r\n', '')
    medals = medals.replace(' ', '')
    medals = medals.replace('\r\n', '')

    records.append((rank, name, surname, country, sport, gold, silver, bronze, medals, url))


# In[37]:


records


# In[38]:


df = pd.DataFrame(records, columns =['rank', 'name', 'surname', 'country', 'sport', 'gold', 'silver', 'bronze', 'medals', 'url'])


# In[39]:


df


# # Changing the URLs parameter

# In[3]:


# Overall
pages = [str(i) for i in range(1,151)]


# In[4]:


start_time = time.time()
requests = 0


# In[5]:


all_ = []
for page in pages:
    all_url = 'https://en.asiangames2018.id/medals/winners/libraries/' + page + '/_overall'
    
    response = get(all_url)

    sleep(randint(8,15))
    
    
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)
    
    medallists_soup = BeautifulSoup(response.text, 'html.parser')
    
    medallists = medallists_soup.find_all('tr', class_ = 'or-e')
    
    for winner in medallists:
        rank = winner.find('span', class_ = 'orp-rk').text
        country = winner.find('img', class_ = 'or-fgs')['title']
        url = 'https://en.asiangames2018.id' + winner.find('a', class_ = 'or-js-w-lk')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya
        name = winner.find('span', class_ = 'or-name').text
        surname = winner.find('span', class_ = 'or-surname').text
        sport = winner.find('a', class_ = 'or-sport-name')['title']
        gold = winner.find('td', class_ = 'or-md or-gold').text
        silver = winner.find('td', class_ = 'or-md or-silver').text
        bronze = winner.find('td', class_ = 'or-md or-bronze').text
        medals = winner.find('td', class_ = 'or-md or-total').text
    
        rank = rank.replace(' ', '')
        rank = rank.replace('\r\n', '')
        gold = gold.replace(' ', '')
        gold = gold.replace('\r\n', '')
        silver = silver.replace(' ', '')
        silver = silver.replace('\r\n', '')
        bronze = bronze.replace(' ', '')
        bronze = bronze.replace('\r\n', '')
        medals = medals.replace(' ', '')
        medals = medals.replace('\r\n', '')

        all_.append((int(rank), name, surname, country, sport, int(gold), int(silver), int(bronze), int(medals), url))


# In[6]:


all_df = pd.DataFrame(all_, columns =['rank', 'name', 'surname', 'country', 'sport', 'gold', 'silver', 'bronze', 'medals', 'url'])


# In[7]:


all_df.to_csv('ag2018_medallists.csv', index=False)


# ## Men

# In[3]:


# Men only
pages = [str(i) for i in range(1,151)]


# In[4]:


start_time = time.time()
requests = 0


# In[5]:


men = []
for page in pages:
    men_url = 'https://en.asiangames2018.id/medals/winners/libraries/' + page + '/_men'
    
    response = get(men_url)

    sleep(randint(8,15))
    
    
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)
    
    medallists_soup = BeautifulSoup(response.text, 'html.parser')
    
    medallists = medallists_soup.find_all('tr', class_ = 'or-e')
    
    for winner in medallists:
        rank = winner.find('span', class_ = 'orp-rk').text
        country = winner.find('img', class_ = 'or-fgs')['title']
        url = 'https://en.asiangames2018.id' + winner.find('a', class_ = 'or-js-w-lk')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya
        name = winner.find('span', class_ = 'or-name').text
        surname = winner.find('span', class_ = 'or-surname').text
        sport = winner.find('a', class_ = 'or-sport-name')['title']
        gold = winner.find('td', class_ = 'or-md or-gold').text
        silver = winner.find('td', class_ = 'or-md or-silver').text
        bronze = winner.find('td', class_ = 'or-md or-bronze').text
        medals = winner.find('td', class_ = 'or-md or-total').text
    
        rank = rank.replace(' ', '')
        rank = rank.replace('\r\n', '')
        gold = gold.replace(' ', '')
        gold = gold.replace('\r\n', '')
        silver = silver.replace(' ', '')
        silver = silver.replace('\r\n', '')
        bronze = bronze.replace(' ', '')
        bronze = bronze.replace('\r\n', '')
        medals = medals.replace(' ', '')
        medals = medals.replace('\r\n', '')

        men.append((int(rank), name, surname, country, sport, int(gold), int(silver), int(bronze), int(medals), url))


# In[6]:


men_df = pd.DataFrame(men, columns =['rank', 'name', 'surname', 'country', 'sport', 'gold', 'silver', 'bronze', 'medals', 'url'])


# In[61]:


men_df.info()


# In[7]:


men_df.to_csv('ag2018_men_medallists.csv', index=False)


# ## Women

# In[8]:


# Women only
pages_wm = [str(i) for i in range(1,148)]


# In[9]:


start_time = time.time()
requests = 0


# In[10]:


women = []
for page in pages_wm:
    women_url = 'https://en.asiangames2018.id/medals/winners/libraries/' + page + '/_women'
    
    response = get(women_url)

    sleep(randint(8,15))
    
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)
    
    medallists_soup = BeautifulSoup(response.text, 'html.parser')
    
    medallists = medallists_soup.find_all('tr', class_ = 'or-e')
    
    for winner in medallists:
        rank = winner.find('span', class_ = 'orp-rk').text
        country = winner.find('img', class_ = 'or-fgs')['title']
        url = 'https://en.asiangames2018.id' + winner.find('a', class_ = 'or-js-w-lk')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya
        name = winner.find('span', class_ = 'or-name').text
        surname = winner.find('span', class_ = 'or-surname').text
        sport = winner.find('a', class_ = 'or-sport-name')['title']
        gold = winner.find('td', class_ = 'or-md or-gold').text
        silver = winner.find('td', class_ = 'or-md or-silver').text
        bronze = winner.find('td', class_ = 'or-md or-bronze').text
        medals = winner.find('td', class_ = 'or-md or-total').text
    
        rank = rank.replace(' ', '')
        rank = rank.replace('\r\n', '')
        gold = gold.replace(' ', '')
        gold = gold.replace('\r\n', '')
        silver = silver.replace(' ', '')
        silver = silver.replace('\r\n', '')
        bronze = bronze.replace(' ', '')
        bronze = bronze.replace('\r\n', '')
        medals = medals.replace(' ', '')
        medals = medals.replace('\r\n', '')

        women.append((int(rank), name, surname, country, sport, int(gold), int(silver), int(bronze), int(medals), url))


# In[11]:


women_df = pd.DataFrame(women, columns =['rank', 'name', 'surname', 'country', 'sport', 'gold', 'silver', 'bronze', 'medals', 'url'])


# In[12]:


women_df.to_csv('ag2018_women_medallists.csv', index=False)


# # Country

# In[13]:


country_ = []
medals_url = 'https://en.asiangames2018.id/medals/'
response = get(medals_url)
country_soup = BeautifulSoup(response.text, 'html.parser')
country_medal = country_soup.find_all('tr', class_ = 'or-ses-list or-js-sch-active orp-plugin')
for country in country_medal:
    rank = country.find('span', class_ = 'orp-rk').text
    id_ = country.find('span', class_ = 'or-team-n').text
    country_name = country.find('span', class_ = 'or-team-n')['title']
    gold = country.find('td', class_ = 'or-md or-gold').text
    silver = country.find('td', class_ = 'or-md or-silver').text
    bronze = country.find('td', class_ = 'or-md or-bronze').text
    medals = country.find('td', class_ = 'or-md or-total or-l').text
    url = 'https://en.asiangames2018.id' + country['data-href']
    
    rank = rank.replace(' ', '')
    rank = rank.replace('\r\n', '')
    gold = gold.replace(' ', '')
    gold = gold.replace('\r\n', '')
    silver = silver.replace(' ', '')
    silver = silver.replace('\r\n', '')
    bronze = bronze.replace(' ', '')
    bronze = bronze.replace('\r\n', '')
    medals = medals.replace(' ', '')
    medals = medals.replace('\r\n', '')

    country_.append((int(rank), id_, country_name, int(gold), int(silver), int(bronze), int(medals), url))
    
country_df = pd.DataFrame(country_, columns =['rank', 'id', 'country_name', 'gold', 'silver', 'bronze', 'medals', 'url'])


# In[14]:


country_df.to_csv('ag2018_country_medal_table.csv', index=False)


# ## per Country

# In[15]:


country_df = pd.read_csv('ag2018_country_medal_table.csv')


# In[16]:


for i in range(0, len(country_df)):
    sport_ = []
    url = country_df['url'][i]
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sport_medal = soup.find_all('tr', class_ = 'or-e or-table-list or-table-list-groupedRow')
    for sport in sport_medal:
        name = sport.find('span', class_ = 'or-text').text
        gold = sport.find('td', class_ = 'or-md or-gold').text
        silver = sport.find('td', class_ = 'or-md or-silver').text
        bronze = sport.find('td', class_ = 'or-md or-bronze').text
        medals = sport.find('td', class_ = 'or-md or-total').text
        
        sport_.append((name, int(gold), int(silver), int(bronze), int(medals)))
    
    sport_df = pd.DataFrame(sport_, columns = ['sport_name', 'gold', 'silver', 'bronze', 'total_medals'])
    name_file = 'AG2018_country_medals\\ag2018_' + str(country_df['rank'][i]) + '.' + country_df['id'][i] + '_medal_table.csv'
    sport_df.to_csv(name_file, index = False)


# # Athletes

# In[3]:


women_df = pd.read_csv('ag2018_women_medallists.csv')


# In[4]:


women_df.head()


# In[5]:


women_df.describe()


# In[4]:


athlete = []
requests = 0
start_time = time.time()

for i in range(0, len(women_df)):
    bio = []
    social = []
    
    ath_url = women_df['url'][i]
    ath_response = get(ath_url)
    ath_soup = BeautifulSoup(ath_response.text, 'html.parser')

    
    sleep(randint(1,4))
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)    
    
    name = ath_soup.find('span', class_ = 'or-athlete-profile__name--name').text
    surname = ath_soup.find('span', class_ = 'or-athlete-profile__name--surname').text
    nationality = ath_soup.find('span', class_ = 'or-athlete-profile__nationality--noc').text
    discipline = ath_soup.find('div', class_ = 'or-athlete-profile__discipline').text
    birth_date = ath_soup.find('span', class_ = 'or-athlete__birth--date').text
    birth_city = ath_soup.find('span', class_ = 'or-athlete__birth--city').text
    
    if ath_soup.find('span', class_ = 'or-athlete__birth--country') is not None:
        birth_country = ath_soup.find('span', class_ = 'or-athlete__birth--country').text
    else: birth_country = ''
    
    age = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[0].text
    height = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[2].text
    weight = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[3].text
    
    birth_country = birth_country[1:-1]
    age = age.replace(' ', '')
    age = age.replace('\r\n', '')
    height = height.replace(' ', '')
    height = height.replace('\r', '')
    height = height.replace('\n', '')
    if (height == '-/-'):
        height_cm = ''
        height = ''
    else:
        height_cm = height[0:height.find("CM")] #kalau height = '-/...' atau height.find("CM") == -1, maka akan menyimpan nilai '-/'
        height = height[len(height_cm) + 3:] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    weight = weight.replace(' ', '')
    weight = weight.replace('\r', '')
    weight = weight.replace('\n', '')
    if (weight == '-/-'):
        weight_kg = ''
        weight_lbs = ''
    else:
        weight_kg = weight[0:weight.find("kg")] #kalau weight = '-/...' atau weight.find("kg") == -1, maka akan menyimpan nilai '-/'
        weight_lbs = weight[weight.find("kg") + 3:weight.find("lbs")] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    
    
    src_containers = ath_soup.find_all('orp')
    
    medal_containers = src_containers[0]
    ath_medal_url = medal_containers['src']


    sleep(randint(1,2))

    
    response = get(ath_medal_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup.find_all('td', class_ = 'or-table-medals__b--medal') != []:
        gold = soup.find_all('td', class_ = 'or-table-medals__b--medal')[0].text
        silver = soup.find_all('td', class_ = 'or-table-medals__b--medal')[1].text
        bronze = soup.find_all('td', class_ = 'or-table-medals__b--medal')[2].text
    else:
        gold = 0
        silver = 0
        bronze = 0
    
    bio_containers = src_containers[1]
    bio_url = bio_containers['src']
    bio_response = get(bio_url)
    bio_soup = BeautifulSoup(bio_response.text, 'html.parser')


    sleep(randint(1,2))

    
    bio_containers = bio_soup.find_all('div', class_ ='or-article__part markdown')
    
    for j in range(0, len(bio_containers)):
        subtitle = bio_containers[j].h2.text #Perlu lebih dirapikan di bagian ini
        content = bio_containers[j].p.text #ada b, ada br, ada \n
        if (subtitle == 'Social'):
            socmed_containers = bio_containers[j].find_all('li')
            for k in range(0, len(socmed_containers)):
                social.append((socmed_containers[k].a['href']))
        else:
            bio.append((subtitle, content))
        
        
    athlete.append((ath_url, name, surname, nationality, discipline, birth_date, birth_city, birth_country, age, height_cm, height, weight_kg, weight_lbs, int(gold), int(silver), int(bronze), bio, social, bio_url))
    #height_cm, weight_kg, dan weight_lbs belum jadi int karena bisa berisikan '-' #kasus #351
    #age belum jadi int karena berisikan '\n' #kasus #768


# In[5]:


len(athlete)


# ### top 100 overall medallists

# In[164]:


athlete_top100_df = pd.DataFrame(athlete, columns = ['url','name', 'surname', 'nationality', 'discipline', 'birth_date', 'birth_city', ' birth_country', 'age', 'height_cm', 'height', 'weight_kg', 'weight_lbs', 'gold', 'silver', 'bronze', 'bio', 'bio_url'])
athlete_top100_df.to_csv('ag2018_athlete_top100.csv', index = False)


# ### all women medallists

# In[6]:


athlete_women_df = pd.DataFrame(athlete, columns = ['url','name', 'surname', 'nationality', 'discipline', 'birth_date', 'birth_city', ' birth_country', 'age', 'height_cm', 'height', 'weight_kg', 'weight_lbs', 'gold', 'silver', 'bronze', 'bio', 'social', 'bio_url'])
athlete_women_df.to_csv('ag2018_athlete_women_medallists.csv', index = False)


#  

# In[27]:


men_df = pd.read_csv('ag2018_men_medallists.csv')


# In[28]:


athlete = []
requests = 0
start_time = time.time()

for i in range(0, len(men_df)):
    bio = []
    social = []
    
    ath_url = men_df['url'][i]
    ath_response = get(ath_url)
    ath_soup = BeautifulSoup(ath_response.text, 'html.parser')

    
    sleep(randint(1,4))
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)    
    
    name = ath_soup.find('span', class_ = 'or-athlete-profile__name--name').text
    surname = ath_soup.find('span', class_ = 'or-athlete-profile__name--surname').text
    nationality = ath_soup.find('span', class_ = 'or-athlete-profile__nationality--noc').text
    discipline = ath_soup.find('div', class_ = 'or-athlete-profile__discipline').text
    birth_date = ath_soup.find('span', class_ = 'or-athlete__birth--date').text
    birth_city = ath_soup.find('span', class_ = 'or-athlete__birth--city').text
    
    if ath_soup.find('span', class_ = 'or-athlete__birth--country') is not None:
        birth_country = ath_soup.find('span', class_ = 'or-athlete__birth--country').text
    else: birth_country = ''
    
    age = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[0].text
    height = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[2].text
    weight = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[3].text
    
    birth_country = birth_country[1:-1]
    age = age.replace(' ', '')
    age = age.replace('\r\n', '')
    height = height.replace(' ', '')
    height = height.replace('\r', '')
    height = height.replace('\n', '')
    if (height == '-/-'):
        height_cm = ''
        height = ''
    else:
        height_cm = height[0:height.find("CM")] #kalau height = '-/...' atau height.find("CM") == -1, maka akan menyimpan nilai '-/'
        height = height[len(height_cm) + 3:] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    weight = weight.replace(' ', '')
    weight = weight.replace('\r', '')
    weight = weight.replace('\n', '')
    if (weight == '-/-'):
        weight_kg = ''
        weight_lbs = ''
    else:
        weight_kg = weight[0:weight.find("kg")] #kalau weight = '-/...' atau weight.find("kg") == -1, maka akan menyimpan nilai '-/'
        weight_lbs = weight[weight.find("kg") + 3:weight.find("lbs")] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    
    
    src_containers = ath_soup.find_all('orp')
    
    medal_containers = src_containers[0]
    ath_medal_url = medal_containers['src']


    sleep(randint(1,2))

    
    response = get(ath_medal_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup.find_all('td', class_ = 'or-table-medals__b--medal') != []:
        gold = soup.find_all('td', class_ = 'or-table-medals__b--medal')[0].text
        silver = soup.find_all('td', class_ = 'or-table-medals__b--medal')[1].text
        bronze = soup.find_all('td', class_ = 'or-table-medals__b--medal')[2].text
    else:
        gold = 0
        silver = 0
        bronze = 0
    
    bio_containers = src_containers[1]
    bio_url = bio_containers['src']
    bio_response = get(bio_url)
    bio_soup = BeautifulSoup(bio_response.text, 'html.parser')


    sleep(randint(1,2))

    
    bio_containers = bio_soup.find_all('div', class_ ='or-article__part markdown')
    
    for j in range(0, len(bio_containers)):
        subtitle = bio_containers[j].h2.text #Perlu lebih dirapikan di bagian ini
        content = bio_containers[j].p.text #ada b, ada br, ada \n
        if (subtitle == 'Social'):
            socmed_containers = bio_containers[j].find_all('li')
            for k in range(0, len(socmed_containers)):
                social.append((socmed_containers[k].a['href']))
        else:
            bio.append((subtitle, content))
        
        
    athlete.append((ath_url, name, surname, nationality, discipline, birth_date, birth_city, birth_country, age, height_cm, height, weight_kg, weight_lbs, int(gold), int(silver), int(bronze), bio, social, bio_url))
    #height_cm, weight_kg, dan weight_lbs belum jadi int karena bisa berisikan '-' #kasus #351
    #age belum jadi int karena berisikan '\n' #kasus #768


# In[29]:


len(athlete)


# In[30]:


athlete_men_df = pd.DataFrame(athlete, columns = ['url','name', 'surname', 'nationality', 'discipline', 'birth_date', 'birth_city', ' birth_country', 'age', 'height_cm', 'height', 'weight_kg', 'weight_lbs', 'gold', 'silver', 'bronze', 'bio', 'social', 'bio_url'])
athlete_men_df.to_csv('ag2018_athlete_men_medallists.csv', index = False)


# # Sport Athletes

# In[20]:


athlete_url = 'https://en.asiangames2018.id/athletes/page/1/'

# Make a list of sports' code
response = get(athlete_url)
soup = BeautifulSoup(response.text, 'html.parser')

sport_containers = soup.find_all('li', class_ = 'or-picto or-sportshub__item ')

sport_ = []
for sport in sport_containers:
    sp_name = sport.find('div', class_ = 'or-res-disc-name').text
    sp_ath_no = sport.find('div', class_ = 'or-res-disc-athletes').text
    sp_ath_no = sp_ath_no[0:sp_ath_no.find(" ")]
    sp_ath_url = 'https://en.asiangames2018.id' + sport.find('a')['href']
    sp_code = sport.find('a')['href'][16:18]
    page_no = math.ceil(int(sp_ath_no)/12)
    sport_.append((sp_ath_url, sp_code, sp_name, sp_ath_no, page_no))
    
sport_df = pd.DataFrame(sport_, columns = ['sp_url', 'sp_code', 'sport_name', 'no_athlete_sp', 'page_no'])
sport_df.to_csv('ag2018_sport_athlete_summary.csv', index = False)


# In[21]:


sport_df


# In[7]:


sport_df = pd.read_csv('ag2018_sport_athlete_summary.csv')


# In[14]:


for j in range(0, len(sport_df)):
    pages_sp = [str(i) for i in range(1, int(sport_df['page_no'][j]) + 1)]
    
    start_time = time.time()
    requests = 0
    
    sp_ath = []
    
    for page in pages_sp:
        sp_ath_url = 'https://en.asiangames2018.id/athletes/sport/' + sport_df['sp_code'][j] + '/page/' + page + '/'
    
        response = get(sp_ath_url)

        sleep(randint(8,15))
    
        requests += 1
        elapsed_time = time.time() - start_time
        print('Request: {}.{}; Frequency: {} requests/s'.format(j, requests, requests/elapsed_time))
        clear_output(wait = True)
    
        athlete_soup = BeautifulSoup(response.text, 'html.parser')
    
        athletes = athlete_soup.find_all('li', class_ = 'or-athletes__item')
    
        for athlete in athletes:
            fname = athlete.find('div', class_ = 'or-card-athlete__name')['title'] #fname = surname + name
            name = athlete.find('div', class_ = 'or-card-athlete__passport-name').text
            surname = athlete.find('div', class_ = 'or-card-athlete__passport-surname').text
            country = athlete.find('img', class_ = 'or-card-athlete__country-flag')['title']
            noc_code = athlete.find('div', class_ = 'or-card-athlete__country-code').text
            discipline = athlete.find('div', class_ = 'or-card-athlete__discipline').text
            sp_code = sport_df['sp_code'][j]
            url = 'https://en.asiangames2018.id' + athlete.find('a', class_ = 'or-athletes__link')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya

            sp_ath.append((url, fname, name, surname, country, noc_code, discipline, sp_code))
        
    sp_ath_df = pd.DataFrame(sp_ath, columns =['url', 'fullname', 'name', 'surname', 'country', 'noc_code', 'discipline', 'discipline_code'])
    name_file = 'AG2018_sport_athletes\\ag2018_' + str(int(j) + 1) + '.' + sport_df['sport_name'][j].replace(' ', '-').replace('/','-') + '_athletes.csv'
    sp_ath_df.to_csv(name_file, index=False)


# In[15]:


sp_ath_df = pd.read_csv('AG2018_sport_athletes\\ag2018_' + str(int(j) + 1) + '.' + sport_df['sport_name'][j].replace(' ', '-').replace('/','-') + '_athletes.csv')


# In[17]:


athlete = []
start_time = time.time()
requests = 0

for i in range(0, len(sp_ath_df)):
    bio = []
    social = []
    
    ath_url = sp_ath_df['url'][i]
    ath_response = get(ath_url)
    ath_soup = BeautifulSoup(ath_response.text, 'html.parser')

    
    sleep(randint(1,4))
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)    
    
    name = ath_soup.find('span', class_ = 'or-athlete-profile__name--name').text
    surname = ath_soup.find('span', class_ = 'or-athlete-profile__name--surname').text
    nationality = ath_soup.find('span', class_ = 'or-athlete-profile__nationality--noc').text
    discipline = ath_soup.find('div', class_ = 'or-athlete-profile__discipline').text
    birth_date = ath_soup.find('span', class_ = 'or-athlete__birth--date').text
    birth_city = ath_soup.find('span', class_ = 'or-athlete__birth--city').text
    
    if ath_soup.find('span', class_ = 'or-athlete__birth--country') is not None:
        birth_country = ath_soup.find('span', class_ = 'or-athlete__birth--country').text
    else: birth_country = ''
    
    age = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[0].text
    height = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[2].text
    weight = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[3].text
    
    birth_country = birth_country[1:-1]
    age = age.replace(' ', '')
    age = age.replace('\r\n', '')
    height = height.replace(' ', '')
    height = height.replace('\r', '')
    height = height.replace('\n', '')
    if (height == '-/-'):
        height_cm = ''
        height = ''
    else:
        height_cm = height[0:height.find("CM")] #kalau height = '-/...' atau height.find("CM") == -1, maka akan menyimpan nilai '-/'
        height = height[len(height_cm) + 3:] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    weight = weight.replace(' ', '')
    weight = weight.replace('\r', '')
    weight = weight.replace('\n', '')
    if (weight == '-/-'):
        weight_kg = ''
        weight_lbs = ''
    else:
        weight_kg = weight[0:weight.find("kg")] #kalau weight = '-/...' atau weight.find("kg") == -1, maka akan menyimpan nilai '-/'
        weight_lbs = weight[weight.find("kg") + 3:weight.find("lbs")] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    
    
    src_containers = ath_soup.find_all('orp')
    
    medal_containers = src_containers[0]
    ath_medal_url = medal_containers['src']


    sleep(randint(1,2))

    
    response = get(ath_medal_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup.find_all('td', class_ = 'or-table-medals__b--medal') != []:
        gold = soup.find_all('td', class_ = 'or-table-medals__b--medal')[0].text
        silver = soup.find_all('td', class_ = 'or-table-medals__b--medal')[1].text
        bronze = soup.find_all('td', class_ = 'or-table-medals__b--medal')[2].text
    else:
        gold = 0
        silver = 0
        bronze = 0
    
    bio_containers = src_containers[1]
    bio_url = bio_containers['src']
    bio_response = get(bio_url)
    bio_soup = BeautifulSoup(bio_response.text, 'html.parser')


    sleep(randint(1,2))

    
    bio_containers = bio_soup.find_all('div', class_ ='or-article__part markdown')
    
    for j in range(0, len(bio_containers)):
        subtitle = bio_containers[j].h2.text #Perlu lebih dirapikan di bagian ini
        content = bio_containers[j].p.text #ada b, ada br, ada \n
        if (subtitle == 'Social'):
            socmed_containers = bio_containers[j].find_all('li')
            for k in range(0, len(socmed_containers)):
                social.append((socmed_containers[k].a['href']))
        else:
            bio.append((subtitle, content))
        
        
    athlete.append((ath_url, name, surname, nationality, discipline, birth_date, birth_city, birth_country, age, height_cm, height, weight_kg, weight_lbs, int(gold), int(silver), int(bronze), bio, social, bio_url))
    #height_cm, weight_kg, dan weight_lbs belum jadi int karena bisa berisikan '-' #kasus #351
    #age belum jadi int karena berisikan '\n' #kasus #768


# In[18]:


athlete_wu_df = pd.DataFrame(athlete, columns = ['url','name', 'surname', 'nationality', 'discipline', 'birth_date', 'birth_city', ' birth_country', 'age', 'height_cm', 'height', 'weight_kg', 'weight_lbs', 'gold', 'silver', 'bronze', 'bio', 'social', 'bio_url'])
athlete_wu_df.to_csv('ag2018_athletes_wu.csv', index = False)


# # Country Athletes

# In[13]:


country_ath_url = 'https://en.asiangames2018.id/athletes/countries/'

# Make a list of countries' code
response = get(country_ath_url)
soup = BeautifulSoup(response.text, 'html.parser')

country_containers = soup.find_all('li', class_ = 'or-countries-list__item')

country_ = []
for country in country_containers:
    noc_name = country.find('div', class_ = 'or-countries-list__name').text
    noc_ath_no = country.find('div', class_ = 'or-countries-list__number-athletes').text
    noc_ath_no = noc_ath_no[0:noc_ath_no.find(" ")]
    noc_ath_url = 'https://en.asiangames2018.id' + country.find('a')['href']
    noc_code = country.find('a')['href'][18:21]
    page_no = math.ceil(int(noc_ath_no)/12)
    country_.append((noc_ath_url, noc_code, noc_name, noc_ath_no, page_no))
    
country_ath_df = pd.DataFrame(country_, columns = ['noc_url', 'noc_code', 'country_name', 'no_athlete_noc', 'page_no'])
country_ath_df.to_csv('ag2018_country_athlete_summary.csv', index = False)


# In[16]:


country_ath_df


# ### all Indonesian athletes

# In[36]:


start_time = time.time()
requests = 0


# In[37]:


pages_ina = [str(i) for i in range(1, country_ath_df['page_no'][45] + 1)]


# In[38]:


ina_ath = []
for page in pages_ina:
    ina_ath_url = 'https://en.asiangames2018.id/athletes/country/INA/page/' + page + '/'
    
    response = get(ina_ath_url)

    sleep(randint(8,15))
    
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)
    
    athlete_soup = BeautifulSoup(response.text, 'html.parser')
    
    athletes = athlete_soup.find_all('li', class_ = 'or-athletes__item')
    
    for athlete in athletes:
        fname = athlete.find('div', class_ = 'or-card-athlete__name')['title'] #fname = surname + name
        name = athlete.find('div', class_ = 'or-card-athlete__passport-name').text
        surname = athlete.find('div', class_ = 'or-card-athlete__passport-surname').text
        country = athlete.find('img', class_ = 'or-card-athlete__country-flag')['title']
        noc_code = athlete.find('div', class_ = 'or-card-athlete__country-code').text
        discipline = athlete.find('div', class_ = 'or-card-athlete__discipline').text
        url = 'https://en.asiangames2018.id' + athlete.find('a', class_ = 'or-athletes__link')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya

        ina_ath.append((url, fname, name, surname, country, noc_code, discipline))
        
ina_ath_df = pd.DataFrame(ina_ath, columns =['url', 'fullname', 'name', 'surname', 'country', 'noc_code', 'discipline'])
ina_ath_df.to_csv('ag2018_ina_athletes.csv', index=False)


# In[56]:


athlete = []
start_time = time.time()
requests = 0

for i in range(0, int(country_ath_df['no_athlete_noc'][45]) + 2): #ada tambahan 2 atlet daripada data yang ada (sepertinya karena ada double)
    bio = []
    social = []
    
    ath_url = ina_ath_df['url'][i]
    ath_response = get(ath_url)
    ath_soup = BeautifulSoup(ath_response.text, 'html.parser')

    
    sleep(randint(1,4))
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)    
    
    name = ath_soup.find('span', class_ = 'or-athlete-profile__name--name').text
    surname = ath_soup.find('span', class_ = 'or-athlete-profile__name--surname').text
    nationality = ath_soup.find('span', class_ = 'or-athlete-profile__nationality--noc').text
    discipline = ath_soup.find('div', class_ = 'or-athlete-profile__discipline').text
    birth_date = ath_soup.find('span', class_ = 'or-athlete__birth--date').text
    birth_city = ath_soup.find('span', class_ = 'or-athlete__birth--city').text
    
    if ath_soup.find('span', class_ = 'or-athlete__birth--country') is not None:
        birth_country = ath_soup.find('span', class_ = 'or-athlete__birth--country').text
    else: birth_country = ''
    
    age = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[0].text
    height = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[2].text
    weight = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[3].text
    
    birth_country = birth_country[1:-1]
    age = age.replace(' ', '')
    age = age.replace('\r\n', '')
    height = height.replace(' ', '')
    height = height.replace('\r', '')
    height = height.replace('\n', '')
    if (height == '-/-'):
        height_cm = ''
        height = ''
    else:
        height_cm = height[0:height.find("CM")] #kalau height = '-/...' atau height.find("CM") == -1, maka akan menyimpan nilai '-/'
        height = height[len(height_cm) + 3:] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    weight = weight.replace(' ', '')
    weight = weight.replace('\r', '')
    weight = weight.replace('\n', '')
    if (weight == '-/-'):
        weight_kg = ''
        weight_lbs = ''
    else:
        weight_kg = weight[0:weight.find("kg")] #kalau weight = '-/...' atau weight.find("kg") == -1, maka akan menyimpan nilai '-/'
        weight_lbs = weight[weight.find("kg") + 3:weight.find("lbs")] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    
    
    src_containers = ath_soup.find_all('orp')
    
    medal_containers = src_containers[0]
    ath_medal_url = medal_containers['src']


    sleep(randint(1,2))

    
    response = get(ath_medal_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup.find_all('td', class_ = 'or-table-medals__b--medal') != []:
        gold = soup.find_all('td', class_ = 'or-table-medals__b--medal')[0].text
        silver = soup.find_all('td', class_ = 'or-table-medals__b--medal')[1].text
        bronze = soup.find_all('td', class_ = 'or-table-medals__b--medal')[2].text
    else:
        gold = 0
        silver = 0
        bronze = 0
    
    bio_containers = src_containers[1]
    bio_url = bio_containers['src']
    bio_response = get(bio_url)
    bio_soup = BeautifulSoup(bio_response.text, 'html.parser')


    sleep(randint(1,2))

    
    bio_containers = bio_soup.find_all('div', class_ ='or-article__part markdown')
    
    for j in range(0, len(bio_containers)):
        subtitle = bio_containers[j].h2.text #Perlu lebih dirapikan di bagian ini
        content = bio_containers[j].p.text #ada b, ada br, ada \n
        if (subtitle == 'Social'):
            socmed_containers = bio_containers[j].find_all('li')
            for k in range(0, len(socmed_containers)):
                social.append((socmed_containers[k].a['href']))
        else:
            bio.append((subtitle, content))
        
        
    athlete.append((ath_url, name, surname, nationality, discipline, birth_date, birth_city, birth_country, age, height_cm, height, weight_kg, weight_lbs, int(gold), int(silver), int(bronze), bio, social, bio_url))
    #height_cm, weight_kg, dan weight_lbs belum jadi int karena bisa berisikan '-' #kasus #351
    #age belum jadi int karena berisikan '\n' #kasus #768


# In[57]:


athlete_ina_df = pd.DataFrame(athlete, columns = ['url','name', 'surname', 'nationality', 'discipline', 'birth_date', 'birth_city', ' birth_country', 'age', 'height_cm', 'height', 'weight_kg', 'weight_lbs', 'gold', 'silver', 'bronze', 'bio', 'social', 'bio_url'])
athlete_ina_df.to_csv('ag2018_athletes_ina.csv', index = False)


# In[6]:


country_ath_df = pd.read_csv('ag2018_country_athlete_summary.csv')


# In[6]:


for j in range(0, len(country_ath_df)):
    pages_noc = [str(i) for i in range(1, int(country_ath_df['page_no'][j]) + 1)]
    
    start_time = time.time()
    requests = 0
    
    noc_ath = []
    
    for page in pages_noc:
        noc_ath_url = 'https://en.asiangames2018.id/athletes/country/' + country_ath_df['noc_code'][j] + '/page/' + page + '/'
    
        response = get(noc_ath_url)

        sleep(randint(8,15))
    
        requests += 1
        elapsed_time = time.time() - start_time
        print('Request: {}.{}; Frequency: {} requests/s'.format(j, requests, requests/elapsed_time))
        clear_output(wait = True)
    
        athlete_soup = BeautifulSoup(response.text, 'html.parser')
    
        athletes = athlete_soup.find_all('li', class_ = 'or-athletes__item')
    
        for athlete in athletes:
            fname = athlete.find('div', class_ = 'or-card-athlete__name')['title'] #fname = surname + name
            name = athlete.find('div', class_ = 'or-card-athlete__passport-name').text
            surname = athlete.find('div', class_ = 'or-card-athlete__passport-surname').text
            country = athlete.find('img', class_ = 'or-card-athlete__country-flag')['title']
            noc_code = athlete.find('div', class_ = 'or-card-athlete__country-code').text
            discipline = athlete.find('div', class_ = 'or-card-athlete__discipline').text
            url = 'https://en.asiangames2018.id' + athlete.find('a', class_ = 'or-athletes__link')['href'] # Perlu ditambahkan 'https://en.asiangames2018.id' di depannya

            noc_ath.append((url, fname, name, surname, country, noc_code, discipline))
        
    noc_ath_df = pd.DataFrame(noc_ath, columns =['url', 'fullname', 'name', 'surname', 'country', 'noc_code', 'discipline'])
    name_file = 'AG2018_country_athletes\\ag2018_' + str(int(j) + 1) + '.' + country_ath_df['noc_code'][j].lower() + '_athletes.csv'
    noc_ath_df.to_csv(name_file, index=False)


# In[5]:


noc_ath


# In[24]:


athlete = []
requests = 0
start_time = time.time()

name_file = 'AG2018_country_athletes\\ag2018_' + str(7) + '.' + country_ath_df['noc_code'][6].lower() + '_athletes.csv'
noc_ath_df = pd.read_csv(name_file)

for i in range(0, len(noc_ath_df)):
    bio = []
    social = []
    
    ath_url = noc_ath_df['url'][i]
    ath_response = get(ath_url)
    ath_soup = BeautifulSoup(ath_response.text, 'html.parser')

    
    sleep(randint(1,4))
    requests += 1
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)    
    
    name = ath_soup.find('span', class_ = 'or-athlete-profile__name--name').text
    surname = ath_soup.find('span', class_ = 'or-athlete-profile__name--surname').text
    nationality = ath_soup.find('span', class_ = 'or-athlete-profile__nationality--noc').text
    discipline = ath_soup.find('div', class_ = 'or-athlete-profile__discipline').text
    birth_date = ath_soup.find('span', class_ = 'or-athlete__birth--date').text
    birth_city = ath_soup.find('span', class_ = 'or-athlete__birth--city').text
    
    if ath_soup.find('span', class_ = 'or-athlete__birth--country') is not None:
        birth_country = ath_soup.find('span', class_ = 'or-athlete__birth--country').text
    else: birth_country = ''
    
    age = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[0].text
    height = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[2].text
    weight = ath_soup.find_all('div', class_ = 'or-anagraphic__data')[3].text
    
    birth_country = birth_country[1:-1]
    age = age.replace(' ', '')
    age = age.replace('\r\n', '')
    height = height.replace(' ', '')
    height = height.replace('\r', '')
    height = height.replace('\n', '')
    if (height == '-/-'):
        height_cm = ''
        height = ''
    else:
        height_cm = height[0:height.find("CM")] #kalau height = '-/...' atau height.find("CM") == -1, maka akan menyimpan nilai '-/'
        height = height[len(height_cm) + 3:] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    weight = weight.replace(' ', '')
    weight = weight.replace('\r', '')
    weight = weight.replace('\n', '')
    if (weight == '-/-'):
        weight_kg = ''
        weight_lbs = ''
    else:
        weight_kg = weight[0:weight.find("kg")] #kalau weight = '-/...' atau weight.find("kg") == -1, maka akan menyimpan nilai '-/'
        weight_lbs = weight[weight.find("kg") + 3:weight.find("lbs")] #sudah benar nampaknya... #perlu dicek lagi kalau algoritma yang di atas ini diganti
    
    
    src_containers = ath_soup.find_all('orp')
    
    medal_containers = src_containers[0]
    ath_medal_url = medal_containers['src']


    sleep(randint(1,2))

    
    response = get(ath_medal_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if soup.find_all('td', class_ = 'or-table-medals__b--medal') != []:
        gold = soup.find_all('td', class_ = 'or-table-medals__b--medal')[0].text
        silver = soup.find_all('td', class_ = 'or-table-medals__b--medal')[1].text
        bronze = soup.find_all('td', class_ = 'or-table-medals__b--medal')[2].text
    else:
        gold = 0
        silver = 0
        bronze = 0
    
    bio_containers = src_containers[1]
    bio_url = bio_containers['src']
    bio_response = get(bio_url)
    bio_soup = BeautifulSoup(bio_response.text, 'html.parser')


    sleep(randint(1,2))

    
    bio_containers = bio_soup.find_all('div', class_ ='or-article__part markdown')
    
    for j in range(0, len(bio_containers)):
        subtitle = bio_containers[j].h2.text #Perlu lebih dirapikan di bagian ini
        content = bio_containers[j].p.text #ada b, ada br, ada \n
        if (subtitle == 'Social'):
            socmed_containers = bio_containers[j].find_all('li')
            for k in range(0, len(socmed_containers)):
                social.append((socmed_containers[k].a['href']))
        else:
            bio.append((subtitle, content))
        
        
    athlete.append((ath_url, name, surname, nationality, discipline, birth_date, birth_city, birth_country, age, height_cm, height, weight_kg, weight_lbs, int(gold), int(silver), int(bronze), bio, social, bio_url))
    #height_cm, weight_kg, dan weight_lbs belum jadi int karena bisa berisikan '-' #kasus #351
    #age belum jadi int karena berisikan '\n' #kasus #768


# In[25]:


len(athlete)


# In[26]:


athlete_chn_df = pd.DataFrame(athlete, columns = ['url','name', 'surname', 'nationality', 'discipline', 'birth_date', 'birth_city', ' birth_country', 'age', 'height_cm', 'height', 'weight_kg', 'weight_lbs', 'gold', 'silver', 'bronze', 'bio', 'social', 'bio_url'])
athlete_chn_df.to_csv('ag2018_athletes_chn.csv', index = False)


# # Coba yang lain

# In[24]:


# specify the url
quote_page = 'https://en.asiangames2018.id/athletes/athlete/SUN-Yang-3008844'


# In[25]:


# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(quote_page)


# In[26]:


print(page)


# In[27]:


# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')


# In[18]:


# Take out the <div> of name and get its value
age_box = soup.find('div', attrs={'class': 'or-anagraphic__data'})


# In[19]:


age = age_box.text.strip() # strip() is used to remove starting and trailing
print(age)


# In[26]:


name_box = soup.find('span', attrs={'class': 'or-athlete-profile__name--name'})
surname_box = soup.find('span', attrs={'class': 'or-athlete-profile__name--surname'})
nationality_box = soup.find('span', attrs={'class': 'or-athlete-profile__nationality--noc'})
discipline_box = soup.find('div', attrs={'class': 'or-athlete-profile__discipline'})


# In[22]:


date_box = soup.find('span', attrs={'class': 'or-athlete__birth--date'})
city_box = soup.find('span', attrs={'class': 'or-athlete__birth--city'})
country_box = soup.find('span', attrs={'class': 'or-athlete__birth--country'})


# In[27]:


name = name_box.text.strip()
surname = surname_box.text.strip()
nationality = nationality_box.text.strip()
discipline = discipline_box.text.strip()
date = date_box.text.strip()
city = city_box.text.strip()
country = country_box.text.strip()


# In[20]:


import csv
from datetime import datetime


# In[37]:


# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, surname, nationality, discipline, age, date, city, country, datetime.now()])


# In[28]:


article_box = soup.find('article')


# In[29]:


print(article_box)


# In[31]:


article = article_box.text.strip()
print(article)


# In[35]:


article2_box = soup.find('div', attrs={'class': 'or-article__part markdown'})


# In[36]:


article2 = article2_box.text.strip()
print(article2)


# # Multiple Indices

# In[ ]:


quote_page = [‘http://www.bloomberg.com/quote/SPX:IND', ‘http://www.bloomberg.com/quote/CCMP:IND']


# In[ ]:


# for loop
data = []

for pg in quote_page:
 # query the website and return the html to the variable ‘page’
 page = urllib2.urlopen(pg)

# parse the html using beautiful soap and store in variable `soup`
 soup = BeautifulSoup(page, ‘html.parser’)

# Take out the <div> of name and get its value
 name_box = soup.find(‘h1’, attrs={‘class’: ‘name’})
 name = name_box.text.strip() # strip() is used to remove starting and trailing

# get the index price
 price_box = soup.find(‘div’, attrs={‘class’:’price’})
 price = price_box.text

# save the data in tuple
 data.append((name, price))


# In[ ]:


# open a csv file with append, so old data will not be erased
with open(‘index.csv’, ‘a’) as csv_file:
 writer = csv.writer(csv_file)
 # The for loop
 for name, price in data:
 writer.writerow([name, price, datetime.now()])


# # Coba pakai requests get()

# In[2]:


url = 'https://en.asiangames2018.id/athletes/athlete/XU-Jiayu-3008858/'
response = get(url)


# In[3]:


print(response.text)


# In[4]:


html_soup = BeautifulSoup(response.text, 'html.parser')


# In[30]:


article_containers = html_soup.find_all('orp')


# In[31]:


print(type(article_containers))
print(len(article_containers))


# In[32]:


print(article_containers)


# In[33]:


medal_containers = article_containers[0]


# In[34]:


medal_containers


# In[42]:


medal_containers['src']


# In[43]:


biography_containers = article_containers[1]
biography_containers['src']


# In[44]:


bio_url = biography_containers['src']


# In[45]:


bio_response = get(bio_url)


# In[46]:


bio_html_soup = BeautifulSoup(bio_response.text, 'html.parser')


# In[47]:


bio_containers = bio_html_soup.find_all('div', class_ ='or-article__part markdown')


# In[49]:


print(len(bio_containers))


# In[53]:


for i in range(0,len(bio_containers)):
    print(bio_containers[i].h2.text) #Coba cek juga bio_containers[i].h2

