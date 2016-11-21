from email_service import *
from argparse import ArgumentParser
from models import *
from secret_santa_matcher import *
from person_loader import *

def print_pairs(pairs):
    print("Matches")
    print("-------")
    for pair in pairs:
        print("Sender: {}, Receiver: {}".format(pair.giver.name, pair.receiver.name))

def generate_message_for_match(match, sender_address):
    return EmailMessage(match.receiver.email,
                        sender_address,
                        "Your Secret Santa is Enclosed!",
                        "Your Secret Santa is {}.".format(match.receiver.name))

def notify_matches(matches, sender_address):
    for match in matches:
        # send email
        pass

def get_argument_parser():
    parser = ArgumentParser()

    parser.add_argument("-f",
                        "--file",
                        help="CSV with Secret Sanata participants")

    parser.add_argument("--suppressoutput", 
                        help="Indicates that matches should not be printed", 
                        action='count')

    parser.add_argument("--sendemail", 
                        help="Indicates an email should be sent to participants", 
                        action='count')

    parser.add_argument("--senderaddress", 
                        help="Email address to send pairings under")

    return parser

if __name__ == "__main__":
    args = get_argument_parser().parse_args()

    pool = load_people_from_csv(args.file)
    matches = match_pairs(pool)

    if (not args.suppressoutput):
        print_pairs(matches)

    if (args.sendemail):
        if (not args.senderaddress):
            print("Specify a sender address using the --senderaddress flag.")
        else:
            notify_matches(matches, args.senderaddress)
