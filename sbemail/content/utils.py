import json
import os.path

def read_sbemails():
    path = os.path.join(os.path.dirname(__file__), 'sbemails.json')
    with open(path, 'r') as f:
        sbemails = json.load(f)
    return sbemails

sbemails = read_sbemails()['emails']