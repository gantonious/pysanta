from email_service import *
from argparse import ArgumentParser
from models import *
from secret_santa_matcher import *
from person_loader import *

def print_pairs(pairs):
    print("Pairs:")
    print("---------")
    for pair in pairs:
        print("Sender: {}, Receiver: {}".format(pair.giver.name, pair.receiver.name))

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="CSV with Secret Sanata participants")
    args = parser.parse_args()

    persons = load_people_from_csv(args.file)
    pairs = match_pairs(persons)
    print_pairs(pairs)
