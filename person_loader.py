import csv
from models import Person

def load_people_from_csv(filepath):
    loaded_people = []

    with open(filepath, 'rt') as csvfile:
        people_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in people_reader:
            loaded_people.append(Person(row[0], row[1]))

    return loaded_people