import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import telebot

bot_token = "" #Enter your bot token 

bot = telebot.TeleBot(bot_token)

data = []

#scrape function

def scrape():

    fetched_url = "https://cvefeed.io/vuln/latest/"
    response = requests.get(fetched_url)


    soup = BeautifulSoup(response.text,'html.parser')
    
    main_div = soup.find('div',class_= "card-body pt-1")

    cve_link = main_div.findAll('a',class_="text-reset stretched-link")
    
    site = "https://cvefeed.io/"
    
    
    
    for link in cve_link:
        cve_title = link.get_text(strip=True)
        cve_url = link['href']
        main_url = urljoin(site,cve_url)
        data.append((cve_title,main_url))
    
    return data
   
def send_data():
    
    chat_id =  #Enter your chat id 

    data = scrape()

    for cve_title,main_url in data:
        message = f"{cve_title}\n{main_url}"
        bot.send_message(chat_id,message)
   

if __name__ == '__main__':
    send_data()
