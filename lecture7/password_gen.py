#nouns = [ "dinosaur", "vehicle", "panda"]
#adjectives = ["sleepy", "tired", "angry", "annoyed", "giggling"]

import os
adjectives_file = os.path.join( os.path.dirname(__file__), 'adjectives.txt')
nouns_file = os.path.join( os.path.dirname(__file__), 'nouns.txt')
import password_utils
from password_utils import read_lines_from_file

import random

#I could specify the folder directly: with open('lecture6/nouns.txt') as f:
def generate_password(nouns_file=nouns_file, adjectives_file=adjectives_file,
                       numbers_until: int = 100):
    nouns = read_lines_from_file(nouns_file)
    adjectives = read_lines_from_file(adjectives_file)
    
    chosen_adj = random.choice(adjectives)
    chosen_noun = random.choice(nouns)
    random_number = random.randint(0, numbers_until+1)
    special_chars = "*/-.$%&?~#§"
    chosen_char = random.choice(special_chars)
    password = chosen_adj + chosen_noun + str(random_number) + chosen_char
    return password

if __name__ == "__main__":
    generated_password = generate_password(nouns_file, adjectives_file)
    print(generated_password)