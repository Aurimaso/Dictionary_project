# Create a public function, that would generate a dictionary with 10 random key value pairs. 
# Keys random letter, values random numbers range 0:30 cannot be the same.
# Rerun Key which has biggest value.

import random, string

def random_dict() -> dict:
    dict = {}
    random_number = random.randint(0,30)
    while True:
        if random_number not in dict.values():
                dict[random.choice(string.ascii_lowercase)] = random.randint(0,30)
        if len(dict) >= 10:
            break
    print(dict)
    return max(dict, key=dict.get)

print(random_dict())










