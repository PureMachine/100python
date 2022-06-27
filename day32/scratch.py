import smtplib

my_email = "conrad@gmail.com"
password = "abcd1234()"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email, password=password)

