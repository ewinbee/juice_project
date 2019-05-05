#! python3

import json


# Loading JSON structure:
with open("juices.json") as json_file:
	data_json = json.load(json_file)


indexdict = {}
juicedict = {}
sub_ingredient_list = []
final_ingredient_list = []

#collecting data from file and plugging into list:
for juice_variety in data_json["hits"]:
	juicedict[juice_variety["fields"]["item_name"]] = juice_variety["fields"]["nf_ingredient_statement"]
	ingreds = juice_variety["fields"]["nf_ingredient_statement"]
	ingredient_list = ingreds.split(",")
	for ingredient in ingredient_list:
		sub_ingredient_list.append(ingredient)

# distinct ingredient list:
final_ingredient_list = set(sub_ingredient_list)

# populating dictionary of juices:
for ingredient in final_ingredient_list:
	indexdict[ingredient] = []
	for juice, ingredlist in juicedict.items():
		if ingredlist.find(ingredient) != -1:
			indexdict[ingredient].append(juice)


text_file = open("item_three.txt", "w")

for key, value in indexdict.items():
	for item in value:
		text_file.write(key + " : " + item + "\n")

text_file.close()
