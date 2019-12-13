import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPException, SMTPAuthenticationError, SMTP
import datetime

class MessageUsers():
    user_details = []
    messages = []
    base_message = """Hi {name}! 

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""
    def add_user(self, name, amount, email):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
                "name" : name,
                "amount" : amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_message = message.format(
                        name = name,
                        date = date,
                        total = amount
                        )
                self.messages.append(new_message)
                # print(new_message)
        return self.messages
        # return[]
host = "smtp.gmail.com"
port = 587
username = "wonwanz0121@gmail.com"
password = "andrew860121"
from_email = username
to_list = []

obj = MessageUsers()
obj.add_user("andrew", 100, email = "andrew40606@gapp.nthu.edu.tw")
obj.add_user("abdrew", 200, email = "abdrew40606@gmail.com")
obj.add_user("flandre", 169, email = "flandre0121@gmail.com")
obj.add_user("wonwanz", 399.99, email = "wonwanz0121@gmail.com")
body_list = obj.make_messages()
details = obj.get_details()

for i in range(len(details)):
	indiv = details[i]
	to_list += [indiv["email"]]

try:
	email_con = smtplib.SMTP(host, port)
	email_con.ehlo()
	email_con.starttls()
	the_msg = MIMEMultipart("alternative")
	the_msg["Subject"] = "Hello uwu! This is your bill"
	the_msg["From"] = from_email
	email_con.login(username, password)
	for i in range(len(to_list)):
		body = body_list[i]
		body_MIME = MIMEText(body, 'plain')
		the_msg = MIMEMultipart("alternative")
		the_msg["Subject"] = "Hello uwu! This is your bill"
		the_msg["From"] = from_email
		the_msg.attach(body_MIME)
		the_msg["to"] = to_list[i]
		email_con.sendmail(from_email, to_list[i], the_msg.as_string())
except smtplib.SMTPException:
	print("An error occured")


