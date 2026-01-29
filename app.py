from urllib import request
import random
#import requests
from bs4 import BeautifulSoup

#download image from url
def image_downloader(link):
    name = random.randrange(200, 2000)
    location = 'image/' + str(name) + '.jpg'
    request.urlretrieve(link, location)

image_downloader('https://templatemo.com/screenshots/templatemo_224_wedding_store.jpg')






'''

link = 'https://sample-files.com/downloads/data/csv/large-dataset.csv'

def download(csvurl):
    response = request.urlopen(csvurl)
    csv = response.read()
    csvstr = str(csv)
    lines = csvstr.split('\\n')
    save = r'mycsv.csv'
    dw = open(save, 'w')
    for line in lines:
        dw.write(line + '\n')
        dw.close()
        
download(link)

'''


'''
def images(url):
    name = random.randrange(1,1000)
    fullname= str(name) + ".jpg"
    urllib.request.urlretrieve(url,fullname)

images('https://templatemo.com/screenshots/templatemo_224_wedding_store.jpg')



fwrite = open('instructions.txt', 'w')
fwrite.write('hello bro\n pay me my money')
fwrite.close()

fread = open('instructions.txt','r')
read = fread.read()
print(read + 'ok')
fread.close()

'''

