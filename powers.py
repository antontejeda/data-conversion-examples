# read superheros.json
import json
from pprint import pprint

with open('superheros.json') as f:
	data = json. load(f)

# create a blank list of powers
powers = []

members = data ['members']
#loop pver members
for member in members:
	#for each member , loop[ over powers
	member_power = member['powers']
	for power in member_power:
		# add that to our List of powers
		powers. append(power)

# get only unique elements
unique_powers = list(set(powers))
pprint(unique_powers)

 


#Emmanuel and Anton