# 3

from bs4 import BeautifulSoup
import requests

def parser():

    try:
        url = "https://www.example.com"

        responce = requests.get(url)
        soup = BeautifulSoup(responce.content, 'lxml') # <- pip install lxml
        items = soup.find_all(class_="example-class")

        if items:
            for item in items:
                print(item.text)
        else:
            print('немає елементів')
    except:
        print("Немаэ пiдключення", "Error 404")

parser()