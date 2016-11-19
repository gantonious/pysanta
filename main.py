from email_service import *
from models import *
from secret_santa_matcher import *
from person_loader import *

# message = EmailMessage("gaflight95@gmail.com", "test@gmail.com", "Testing", "Testing12345")
# service = EmailService()
# service.send_email(message)

def print_pairs(pairs):
    print("Pairs:")
    print("---------")
    for pair in pairs:
        print("Sender: {}, Receiver: {}".format(pair.giver.name, pair.receiver.name))

persons = load_people_from_csv("participating.csv")
pairs = match_pairs(persons)
print_pairs(pairs)
