import requests
import time

#variables
api_key = ' site api '
bot_key = ' telegram bot key '
chat_id = ' telegram bot id '
limit=10000
time_interval= 1

#function to get price of coin 
def get_price():
  url="https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

  parameters = {
  'start':'1',
  'limit':'2',
  'convert':'USD'
}
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
  }
  response= requests.get(url,headers=headers).json()
  btc_price=response['data'][0]['quote']['USD']['price']
  return btc_price
 
 #print the new price if you want to run it only 
 #print(get_price()

#this fuction to send the price to the tele bot 
def send_price(chat_id, msg):
   url= f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
   requests.get(url)


#this fuction linke the price function to send fuction 
def main(): 
    while True:
     price=get_price()
     print(price)
     if price<limit :
         send_price(chat_id, f"the coin now is :{price}")
     time.sleep(time_interval)
  
main()
