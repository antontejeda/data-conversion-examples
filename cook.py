import csv
import json

with open('veggies.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    

with open('veggies.json', 'w') as f:
    json.dump(rows, f, indent=2)
