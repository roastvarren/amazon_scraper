import requests
from bs4 import BeautifulSoup
import smtplib
import time # if user wants to automate program to regularly check price

URL = 'url-of-amazon-product'

headers = {"User-Agent": 'insert-user-agent-here'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="buyNewSection").get_text()
    price_str = price.strip()
    price_float = float(price_str[1:]) # takes out £ sign

    if price_float < 13.00: # price boundary
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@gmail.com', 'emailpassword')

    subject = "PRICE CHANGE"
    body = "Check Amazon link:\n\n" + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('email.from@gmail.com', 'email.to@gmail.com', msg)
    print("EMAIL SUCCESSFULLY SENT")
    server.quit()

check_price()
