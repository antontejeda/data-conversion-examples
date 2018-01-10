vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "kale"},
 {"name": "beer"},
 {"name": "coke"},
]


import csv

with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'length'])
    for veggie in vegetables:
    	#I want name of vegetable and length of that word.
    	vegetable_name = veggie["name"]
    	veggie_name_length = len(vegetable_name)
    	#write those to CSV
    	row = [vegetable_name, veggie_name_length]
    	writer.writerow(row)
