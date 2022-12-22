
import requests

url = 'http://127.0.0.1:5000/getKeywordsFromUrl'
myobj = {'url': "https://www.deepawaliseotips.com"}

x = requests.post(url, json = myobj)

print(x.text)




"""import requests

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

while True:
    while True:
        try:
            page_link = "https://www.deepawaliseotips.com/"
            fetched = uReq(page_link)
            content = fetched.read()
            fetched.close()
            content_html = soup(content,'html.parser')
            text = content_html.find_all('p')

            word_list = str(text)
            break
        except ValueError:
            print('\nPlease enter a valid URL')

    word_count = word_list.split()
    
    for i in word_list:
        print(i)
    find = input('\nWhat keyword are you looking for?: ')
    
    if find in word_list:
        density = word_list.count(find)
        words_in_keyword = find.split()
        a = len(word_count)
        b = len(words_in_keyword)
        while True:
            try:
                c = round(a//b,4)
                d = round(density / c,4)
                e = round(d,4)
                f = e * 100
                print('\n' + str(round(f,3)) + '%' + ' keyword density')
                print('\nThe keyword appears ' + str(density) + ' times in the page.')
                break
            except ZeroDivisionError:
                print('\nDivision by Zero Error, Please input a valid keyword')
                break
    else:
        print('\n' + str(find) + ' does not appear in the URL, try again.')
"""

'''from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
import requests



def text_cleaning(text):
    try:
        # removing more than one newline or spaces
        text = re.sub(r'[\n\r]+', '\n', text)
        url = 'https://mahesh5077.pythonanywhere.com/keywordsFromText'
        myobj = {'text': text, 'word_count':4, 'duplication':0.9, 'max_keywords':100}

        x = requests.post(url, json = myobj)

        da = x.json()
        print(da)
        for i in da['keywords']:
            print(i[0],'------->',text.count(i[0]))

    except Exception as e:
        print(e)
        print(f"Failed to clean")
    #return text

def get_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }

    with HTMLSession() as session:
        try:
            res = session.get(url, headers=headers, timeout=200)
            return text_cleaning(BeautifulSoup(res.content, 'html.parser').text)
        except:
            return text_cleaning(BeautifulSoup('', 'html.parser').text)
        finally:
            print(f"Done Scrapping")

print(get_page_content("https://www.deepawaliseotips.com/"))'''





