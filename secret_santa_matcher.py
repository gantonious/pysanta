from models import *
from random import shuffle

def randomize_pool(people_pool):
    random_pool = people_pool[:]
    shuffle(random_pool)
    
    return random_pool

def match_pairs(people_participating):
    pool = randomize_pool(people_participating)
    pool_size = len(pool)

    return [SecretSantaPair(pool[i],
                            pool[(i + 1) % pool_size])
                            for i in range(pool_size)]
