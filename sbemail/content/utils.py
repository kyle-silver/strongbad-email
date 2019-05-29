import json
import os.path
from random import randint

def read_sbemails():
    path = os.path.join(os.path.dirname(__file__), 'sbemails.json')
    with open(path, 'r') as f:
        sbemails = json.load(f)
    return sbemails

# exported variable
sbemails = read_sbemails()['emails']

def random_sbemail():
    index = randint(0, len(sbemails)-1)
    return sbemails[index]