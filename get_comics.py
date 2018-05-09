import requests
from PIL import Image
from bs4 import BeautifulSoup
import io
import sys
def spider(argv):
        page=1
        max_page=sys.argv[1]
        max_pages=int(max_page)
        path=sys.argv[2]
        url='https://xkcd.com/'
        while page<=max_pages:
                #print(url)
                source_code=requests.get(url)
                plain_text=source_code.text
                soup=BeautifulSoup(plain_text,"lxml")
                imgs = soup.findAll('div',{'id':'comic'})
                #print(imgs)
                lik=imgs[0].img['src']
                name=lik[23:]

                #print(lik)
                
                link='https:'+lik
                response=requests.get(link)
                im=Image.open(io.BytesIO(response.content))
                im.save(path+'/'+name)
                x=soup.find('a',{'accesskey':'p'})
                x=x['href']
                url='https://xkcd.com/'+str(x)
                page+=1

if __name__=='__main__':
        spider(sys.argv[1:])