class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return self.name == other.name and \
                self.email == other.email

    def __hash__(self):
        return hash(self.name) ^ \
                hash(self.email)

class SecretSantaPair:
    def __init__(self, giver, receiver):
        self.giver = giver
        self.receiver = receiver

class EmailMessage:
    def __init__(self, to_address, from_address, subject, body):
        self.to_address = to_address
        self.from_address = from_address
        self.subject = subject
        self.body = body
