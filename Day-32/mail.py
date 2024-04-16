import smtplib

my_email = "sandeepjammi@gmail.com"
password = "oqivagixmfncatxi"

with smtplib.SMTP("smtp.gmail.com") as connection:

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="sandeepjammi6@gmail.com", 
        msg="Subject:Hello\n\nThis is body of my email"
        )
    connection.close()
