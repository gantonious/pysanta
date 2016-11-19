class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailMessage:
    def __init__(self, to_address, from_address, subject, body):
        self.to_address = to_address
        self.from_address = from_address
        self.subject = subject
        self.body = body
