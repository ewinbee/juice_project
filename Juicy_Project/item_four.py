#! python3

import json
import re

from flask import Flask
from flask import render_template
app = Flask(__name__)


# Loading JSON structure:
with open("juices.json") as json_file:
	data_json = json.load(json_file)


indexdict = {}
juicedict = {}
semifinal_ingredient_list = []
final_ingredient_list = []
sorted_ingredient_list = []


# Scrubbing data
for juice_variety in data_json["hits"]:

	juicedict[juice_variety["fields"]["item_name"]] = juice_variety["fields"]["nf_ingredient_statement"].lower()
	ingreds = juice_variety["fields"]["nf_ingredient_statement"]

	if ingreds != "None":

		# As the text within parentheses often contains commas, which we are splitting by,
		# it was necessary to remove all content within parentheses before splitting:
		rep_ingreds = re.sub("[\(].*?[\)]", "", ingreds.lower())
		comp_ingred_list = rep_ingreds.split(",")
		
		for comp_ingred in comp_ingred_list:
			simple_ingred_list = comp_ingred.split(" and ")

			for simple_ingred in simple_ingred_list:
				trimmed_ingred = simple_ingred.strip()

				if trimmed_ingred.endswith("."):
					semifinal_ingredient_list.append(trimmed_ingred[:-1].strip())
				else:
					semifinal_ingredient_list.append(trimmed_ingred.strip())


for ingredient in semifinal_ingredient_list:

	if ingredient != '':

		# As most of the juices were present by themselves as well as
		# with "from concentrate", I removed that phrase to prevent duplicates:
		if ingredient.endswith(" from concentrate"):
			final_ingredient_list.append(ingredient[:-17])
		else:
			final_ingredient_list.append(ingredient)

# I used a set to return distinct ingredients:
final_ingredient_set = set(final_ingredient_list)

sorted_ingredient_list = sorted(final_ingredient_set)


# populating the index:
for ingredient in sorted_ingredient_list:
	indexdict[ingredient] = []

	for juice, ingredlist in juicedict.items():

		if ingredlist.find(ingredient) != -1:
			indexdict[ingredient].append(juice)

	if len(indexdict[ingredient]) == 0:
		indexdict.pop(ingredient)


jsdict = json.dumps(indexdict)


@app.route('/')
def index(ingredient_dict=indexdict):
    return render_template('juice_template.html',ingredient_list=sorted_ingredient_list,js_dict=jsdict)
