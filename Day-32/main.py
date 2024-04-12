import smtplib

my_email = "sandeepjammi@gmail.com"
password = "oqivagixmfncatxi"

connection =  smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="sandeepjammi6@gmail.com", msg="Hello")
connection.close()
