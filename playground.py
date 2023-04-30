from random import randint
import planetmaker
from shipbuilder import maksship
from governments import GovernmentMaker
import moonmaker
import math
import formulas
# y = []

import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(json_object)
