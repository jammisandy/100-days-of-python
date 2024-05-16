import requests
import smtplib 
import lxml
from bs4 import BeautifulSoup
MY_EMAIL = "sandeepjammi@gmail.com"
MY_PASSWORD = PASSWD
DEST_EMAIL = "sandeepjammi6@gmail.com"



url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
#print(price_as_float)

Buy_price = 200

if price_as_float < Buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=DEST_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

