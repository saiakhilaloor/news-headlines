import requests
import subprocess
from bs4 import BeautifulSoup
import time
import vlc
from gtts import gTTS
from mutagen.mp3 import MP3

def reader(s):
    text = gTTS(text=s, lang='en')
    text.save("news.mp3")                  
    player = vlc.MediaPlayer("news.mp3")       
    file = MP3("news.mp3")
    n = file.info.length                        
    player.play()                                  
    time.sleep(n+2.5) 

url="http://www.ndtv.com/top-stories"
page=requests.get(url)
html=BeautifulSoup(page.content,'html.parser')
a=html.find('div',{'class':'new_storylising'})
b=a.find_all('div',{'class':'nstory_header'})
reader("Welcome, Today's top stories are ")
for i in range(len(b)):
	subprocess.Popen(['notify-send',"Today's Top Stories",b[i].text])
	x=b[i].text
	reader(x)
reader('Thats the news for today, Thank you')
