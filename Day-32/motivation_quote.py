import smtplib
import random
import datetime as dt
now = dt.datetime.now()
weekday = now.weekday()

MY_EMAIL = "sandeepjammi@gmail.com"
MY_PASSWORD = "oqivagixmfncatxi"
TO_EMAIL = "chavasankeerthana@gmail.com"


if weekday == 1:
    with open("100-days-of-python/Day-32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )


