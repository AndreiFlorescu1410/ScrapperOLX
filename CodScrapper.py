 # Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


import requests
from bs4 import BeautifulSoup
medii = []


#iPhone X
URL = 'https://www.olx.ro/oferte/q-iphone-x/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
soup

nr_pagini = int(soup.findAll("a", {"data-cy": "page-link-last"})[0].text.replace('\n', ''))
lungime = 0
rezultate_finale = []
for pagina in range(30):
    printProgressBar(pagina + 1, 150, prefix = 'Progress:', suffix = 'Complete', length = 50)
    URL = 'https://www.olx.ro/oferte/q-iphone-x/?page=' + str(pagina)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    rezultate = soup.findAll("p", {"class": "price"})
    lungime = len(rezultate)
    for i in range(lungime):
        rezultat_curent = rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","")
        if (not (rezultat_curent.isalpha())):
            rezultat_curent = float(rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","").replace(',','.'))
            if  rezultat_curent >= 2000 and rezultat_curent <= 7000:
                rezultate_finale.append(rezultat_curent)

media = sum(rezultate_finale)/(len(rezultate_finale))
medii.append(media)

#iPhone Xs
URL = 'https://www.olx.ro/oferte/q-iphone-xs/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
soup

nr_pagini = int(soup.findAll("a", {"data-cy": "page-link-last"})[0].text.replace('\n', ''))
lungime = 0
rezultate_finale = []
for pagina in range(30):
    printProgressBar(pagina + 31, 150, prefix = 'Progress:', suffix = 'Complete', length = 50)
    URL = 'https://www.olx.ro/oferte/q-iphone-xs/?page=' + str(pagina)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    rezultate = soup.findAll("p", {"class": "price"})
    lungime = len(rezultate)
    for i in range(lungime):
        rezultat_curent = rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","")
        if (not (rezultat_curent.isalpha())):
            rezultat_curent = float(rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","").replace(',','.'))
            if  rezultat_curent >= 2000 and rezultat_curent <= 7000:
                rezultate_finale.append(rezultat_curent)
media = sum(rezultate_finale)/(len(rezultate_finale))
medii.append(media)

#iPhone Xs Max
URL = 'https://www.olx.ro/oferte/q-iphone-xs-max/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
soup

nr_pagini = int(soup.findAll("a", {"data-cy": "page-link-last"})[0].text.replace('\n', ''))
lungime = 0
rezultate_finale = []
for pagina in range(30):
    printProgressBar(pagina + 61, 150, prefix = 'Progress:', suffix = 'Complete', length = 50)
    URL = 'https://www.olx.ro/oferte/q-iphone-xs-max/?page=' + str(pagina)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    rezultate = soup.findAll("p", {"class": "price"})
    lungime = len(rezultate)
    for i in range(lungime):
        rezultat_curent = rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","")
        if (not (rezultat_curent.isalpha())):
            rezultat_curent = float(rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","").replace(',','.'))
            if  rezultat_curent >= 2000 and rezultat_curent <= 7000:
                rezultate_finale.append(rezultat_curent)
media = sum(rezultate_finale)/(len(rezultate_finale))
medii.append(media)


#iPhone 11 Pro
URL = 'https://www.olx.ro/oferte/q-iphone-11-pro/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
soup

nr_pagini = int(soup.findAll("a", {"data-cy": "page-link-last"})[0].text.replace('\n', ''))
lungime = 0
rezultate_finale = []
for pagina in range(30):
    printProgressBar(pagina + 91, 150, prefix = 'Progress:', suffix = 'Complete', length = 50)
    URL = 'https://www.olx.ro/oferte/q-iphone-11-pro/?page=' + str(pagina)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    rezultate = soup.findAll("p", {"class": "price"})
    lungime = len(rezultate)
    for i in range(lungime):
        rezultat_curent = rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","")
        if (not (rezultat_curent.isalpha())):
            rezultat_curent = float(rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","").replace(',','.'))
            if  rezultat_curent >= 2000 and rezultat_curent <= 7000:
                rezultate_finale.append(rezultat_curent)
media = sum(rezultate_finale)/(len(rezultate_finale))
medii.append(media)

#iPhone 11 Pro Max

URL = 'https://www.olx.ro/oferte/q-iphone-11-pro-max/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
soup

nr_pagini = int(soup.findAll("a", {"data-cy": "page-link-last"})[0].text.replace('\n', ''))
lungime = 0
rezultate_finale = []
for pagina in range(30):
    printProgressBar(pagina + 121, 150, prefix = 'Progress:', suffix = 'Complete', length = 50)
    URL = 'https://www.olx.ro/oferte/q-iphone-11-pro-max/?page=' + str(pagina)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    rezultate = soup.findAll("p", {"class": "price"})
    lungime = len(rezultate)
    for i in range(lungime):
        rezultat_curent = rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","")
        if (not (rezultat_curent.isalpha())):
            rezultat_curent = float(rezultate[i].text[1:len(rezultate[i].text)-5].replace(" ","").replace(',','.'))
            if  rezultat_curent >= 2000 and rezultat_curent <= 7000:
                rezultate_finale.append(rezultat_curent)
media = sum(rezultate_finale)/(len(rezultate_finale))
medii.append(media)

#Urcam datele in Google Drive
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
work_sheet = client.open('olxScrapper').sheet1

#formatez data si linia pe care trebuie sa adaug
from datetime import date, timedelta
yesterday = date.today() - timedelta(days=1)
yesterday = str(yesterday.day) + '.0' + str(yesterday.month) + '.' + str(yesterday.year)
today = str(date.today().day) + '.0' + str(date.today().month) + '.' + str(date.today().year)
todayrow = str(int(str(work_sheet.find(yesterday))[7:9])+1)

#adaug datele in linia 'yesterdayrow'
for i,j in zip(enumerate(medii),'BCDEF'):
    work_sheet.update_acell(j + todayrow, i[1])
#adaug data de astazi
work_sheet.update_acell('A' + todayrow, today)
