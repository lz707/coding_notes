import smtplib
import datetime as dt
import random

my_email = "abc@gmail.com"
pwd = "abc1234"


now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        chosen_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
    connection.login(my_email, pwd)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="abc@yahoo.com",
        msg = f"Subject: Monday Quotes \n\n {chosen_quote}"
    )