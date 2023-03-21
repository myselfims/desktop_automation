import ctypes
import requests
from datetime import date
from bs4 import BeautifulSoup
import random


crnt_page = 0
photos = 0
target_link = 'https://hdqwalls.com/category/digital-universe-wallpapers'

img_links=[]

while True:   
    try:
        d = date.today()
        if len(img_links) == 0:
            r = requests.get(target_link)
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            div = soup.find_all('div',{'class':'wall-resp col-lg-4 col-md-4 col-sm-4 col-xs-6 column_padding'})
            # print(div)
            print('links added')
            for f in div:
                a = f.find('a')
                img_links.append(a.get('href'))
            

        link = random.choice(img_links)
        # print(link)
        with open(r"E:\Python Projects\Jarvis Project\used_bg.txt",'r+') as f:
            lines = f.read().splitlines()
            last_line = lines[-1]
            print('Checking previous data...')
            if str(link) not in str(f.read()) and int(last_line[-3:]) < int(d.day):
            # if str(link) not in str(f.read()):
                f.write(link+f' Day : {d.day} \n')
                f.close()
                r = requests.get('https://hdqwalls.com/'+link)
                print('Data updated...')
                print('Fetching wallpaper...')
                soup2 = BeautifulSoup(r.content, 'html.parser')
                link = soup2.find('a',{'class':'btn btn-fresh btn-default-res'}).get('href') 
                newr = requests.get(link)
                with open(r'E:\Python Projects\Jarvis Project\wallpaper.jpg', 'wb') as photo:
                    photo.write(newr.content)
                    print('Wallapaer Fetched...')
                    path = r'E:\Python Projects\Jarvis Project\wallpaper.jpg'
                    ctypes.windll.user32.SystemParametersInfoW(20,0, path ,0)
                    print('wallpaper set')
                    photo.close()
                    break
                    
            elif int((len(f.readlines()) / 18)) > 1 :      
                photos = 0
                img_links.clear()
                target_link = 'https://hdqwalls.com/category/digital-universe-wallpapers/page/'+str(int((len(f.readlines()) / 18)))
    except Exception as e:
        # print(e)
        ...
  