from random import randrange
from models import *

def match_pairs(people_participating):
    if (len(people_participating) % 2 != 0):
        return []

    input_people_1 = people_participating[:]
    input_people_2 = people_participating[:]
    
    output_pairs = []

    for person in input_people_1:
        random_index = 0
        receiving_person = person
        
        while (receiving_person == person):
            random_index = randrange(0, len(input_people_2))
            receiving_person = input_people_2[random_index]
        
        output_pairs.append(SecretSantaPair(person, receiving_person))
        input_people_2.remove(receiving_person)

    return output_pairs