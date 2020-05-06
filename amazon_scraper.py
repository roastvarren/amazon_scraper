import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Code-Language-Computer-Hardware-Software/dp/0735611319?pf_rd_r=EH4GGJ95JY9D0VB6CP8S&pf_rd_p=ad1dac78-5484-4aaa-bf17-e82a62646aa9&pd_rd_r=33ef6b46-f196-4d2d-a2d1-b1074220c840&pd_rd_w=ncE49&pd_rd_wg=XH4AC&ref_=pd_gw_ci_mcx_mr_hp_d'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="buyNewSection").get_text()
    price_str = price.strip()
    price_float = float(price_str[1:]) * 100

    if price_float < 1300:
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('michaellan.uk@gmail.com', 'hfglndjsamkdawjg')

    subject = "PRICE CHANGE"
    body = "Check Amazon link:\n\n" + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('michaellan.uk@gmail.com', 'michael.lan1010@gmail.com', msg)

    server.quit()

check_price()
