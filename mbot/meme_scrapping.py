import re
#import requests
import urllib.request
from bs4 import BeautifulSoup
site = 'https://me.me'

def scrape():
    response = urllib.request.urlopen(site)
    soup = BeautifulSoup(response, 'html.parser')
    #print(soup.contents)

    img_tags = soup.find_all('img')
    urls = [img['src'] for img in img_tags]
    #for url in urls:
        #print(url, ",\n")

    meme_dir = "memes/"
    last_image_url = ""
    local_urls = list()
    for url in urls[:10]:
        if "static" in url or last_image_url == url:
            continue
        last_image_url = url
        url = url.replace("thumb_", "")
        if re.search(r'/([\w_-]+[.](jpg|gif|png))', url):
            #with open(meme_dir + filename.group(1), 'wb') as f:
            if 'http' not in url:
                # sometimes an image source can be relative
                # if it is provide the base url which also happens
                # to be the site variable atm.
                url = '{}{}'.format(site, url)
            #response = requests.get(url)
            #f.write(response.content)

            #downloads the contents of the url
            local_url =  "memes/"+url.split("/")[-1]
            urllib.request.urlretrieve(url, local_url)
            local_urls.append(local_url)
    return local_urls
