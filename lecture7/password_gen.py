#nouns = [ "dinosaur", "vehicle", "panda"]
#adjectives = ["sleepy", "tired", "angry", "annoyed", "giggling"]

import os
adjectives_file = os.path.join( os.path.dirname(__file__), 'adjectives.txt')
nouns_file = os.path.join( os.path.dirname(__file__), 'nouns.txt')
import password_utils
from password_utils import read_lines_from_file

#I could specify the folder directly: with open('lecture6/nouns.txt') as f:
nouns = read_lines_from_file(nouns_file)
adjectives = read_lines_from_file(adjectives_file)

print(f"Nouns: {nouns}")
print(f"Adjectives: {adjectives}")