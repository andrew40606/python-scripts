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
    def add_user(self, name, amount, email = None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
                "name" : name,
                "amount" : amount,
        }
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email != None:
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
                print(new_message)
#            print(self.messages)
        return[]
obj = MessageUsers()
obj.add_user('Justin', 123.45)
obj.add_user('John', 94.23)
obj.add_user('Emilee', 124.32)
obj.add_user('Jim', 323.4)
obj.add_user('Ron', 23)
obj.add_user('Sandra', 322.122)
obj.add_user('Whitney', 99.99)
obj.make_messages()