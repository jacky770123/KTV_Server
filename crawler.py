from bs4 import BeautifulSoup
import requests
import urllib

def crawler(song):
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


if __name__ == '__main__':
    crawler("告白氣球")