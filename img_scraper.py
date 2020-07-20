from bs4 import BeautifulSoup
import requests
import re
import urllib
import os
foundlinks=[""]
for url in foundlinks:
    try:
        cookies = dict(cookies="cookies")
        resp = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(resp.content,features="lxml")
        for img in soup.find_all('img', src=True):
            if "http" in str(img):
                imli=str(img.get('src', img.get('src')))
            if "http" not in str(img):
                imli=url+str(img.get('src', img.get('src')))
            try:
                if "?" in imli.split('/')[-1]:
                    pngfilename=imli.split('/')[-1]
                    pngfilename=pngfilename.split("?")[-2]
                else:
                    pngfilename = imli.split('/')[-1]
                if imli!="None":
                    if os.path.exists("img/"+pngfilename)==False:
                        print(imli+"\n")
                        pngr = requests.get(imli,allow_redirects=True)
                        open("img/"+pngfilename, 'wb').write(pngr.content)
            except:
                print("\n\n"+"[img copy] error with "+ str(imli) +"\n\n")
        for extlink in soup.find_all('a', href=True):
            lin=str(extlink.get('href', extlink.get('href')))
            if "http" in str(extlink):
                lin=str(lin)
                lin=lin.replace("https://","~AB~AB~AB~AB~AB~AB~")
                lin=lin.replace("http://","~A~A~A~A~A~A~")
                if "//"in lin:
                    lin=lin.replace("//","/")
                lin=lin.replace("~AB~AB~AB~AB~AB~AB~","https://")
                lin=lin.replace("~A~A~A~A~A~A~","http://")
            if "http" not in str(extlink):
                lin=url+str(lin)
                lin=lin.replace("https://","~ABA~ABA~ABA~ABA~ABA~ABA~")
                lin=lin.replace("http://","~ABAB~ABAB~ABAB~ABAB~ABAB~ABAB~")
                if "//"in lin:
                    lin=lin.replace("//","/")
                lin=lin.replace("~ABA~ABA~ABA~ABA~ABA~ABA~","https://")
                lin=lin.replace("~ABAB~ABAB~ABAB~ABAB~ABAB~ABAB~","http://")
            foundlinks.append(str(lin))
    except:
        print("\n\n"+"[page] error with "+ str(url) +"\n\n")