from bs4 import BeautifulSoup
import requests
import urllib
import lrc2dic

def crawlerYT(song):
    song = urllib.parse.quote(song)         #encode Chinese URL
    result = requests.get("https://www.youtube.com/results?search_query=" + song)   #get HTML source
    c = result.content

    soup = BeautifulSoup(c, "html.parser")

    all_div = soup.findAll('a', class_='yt-uix-tile-link')
    all_time = soup.findAll(class_=('video-time'))
    span = soup.select('span.yt-thumb-simple > img')
    category = soup.findAll('span', class_='accessible-description')

    result = []

    j=0
    for i in range(0,len(category)):
        if category[i].text[3] == 'P':
            j+=1
            continue

        title = all_div[i].text
        address = all_div[i].get('href')
        address = 'https://www.youtube.com' + address
        time = all_time[i-j].text

        if len(str(span[i].get('src'))) > 40:
            img = span[i].get('src')
        else:
            img = span[i].get('data-thumb')
        
        tempdict = {
            'title' : title,
            'address' : address,
            'time' : time,
            'img' : img
        }
        result.append(tempdict)
    return result

def crawlerMojim(lang, song):
    #if lang == 'cht':
    address = "https://mojim.com/" + song + ".html?t3"
    result = requests.get(address)   #get HTML source
    c = result.content

    soup = BeautifulSoup(c, "html.parser")

    all_singer = soup.select('span.mxsh_ss2 > a')
    all_album = soup.select('span.mxsh_ss3 > a')
    all_title = soup.select('span.mxsh_ss4 > a')
    all_time = soup.select('span.mxsh_ss5')

    result = []

    for i in range(0,len(all_singer)):
        singer = all_singer[i].text
        album = all_album[i].text
        title = all_title[i].text
        address = all_title[i].get('href')
        time = all_time[i+1].text
        
        tempdict = {
            'singer' : singer,
            'album' : album,
            'title' : title,
            'address' : address,
            'time' : time
        }
        result.append(tempdict)
    return result
    
def getLyrics(lang, href):
    address = "https://mojim.com" + href
    result = requests.get(address)   #get HTML source
    c = result.content

    soup = BeautifulSoup(c, "html.parser")

    lyrics = soup.find('dl', class_='fsZx1')
    lyrics.ol.decompose()
    lyrics.dt.decompose()
    lyrics = str(lyrics)
    
    head = lyrics.find('[')
    tail = lyrics.rfind(']')
    if head == -1 or tail == -1:
        return -1, None

    lyrics = lyrics[head:tail+1]
    lyrics = lyrics.replace("<br/>", "\n")

    if lyrics.find('---') != (-1):
        return 0, lyrics    # need to modify by manual
    else:
        return 1, lyrics

if __name__ == '__main__':
    #crawlerYT('告白氣球')
    #crawlerMojim(1, '告白氣球')
    num, tempStr = getLyrics(1, '/twy104616x4x3.htm')  #小情歌
    #num, tempStr = getLyrics(1, '/twy100951x21x1.htm')  # 不能說的秘密 (two lyrics)
    #num, tempStr = getLyrics(1, '/twy100951x39x8.htm')
    dic = lrc2dic.lrc2dict(tempStr)
    