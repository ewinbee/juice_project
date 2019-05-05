#! python3

import json


# Loading JSON structure:
with open("juices.json") as json_file:
	data_json = json.load(json_file)

fl_oz = 0.0
calories = 0.0

# Values acquired through internet research, these are estimates:
for juice_variety in data_json["hits"]:

	if juice_variety["fields"]["nf_serving_size_unit"] == "fl oz":
		fl_oz += juice_variety["fields"]["nf_serving_size_qty"]
		calories += juice_variety["fields"]["nf_calories"]

	elif juice_variety["fields"]["nf_serving_size_unit"] == "bottle":
		fl_oz += 10.0
		calories += juice_variety["fields"]["nf_calories"]

	elif juice_variety["fields"]["nf_serving_size_unit"] == "pop":
		fl_oz += 1.5
		calories += juice_variety["fields"]["nf_calories"]

	elif juice_variety["fields"]["nf_serving_size_unit"] == "pouch":
		fl_oz += 6.0
		calories += juice_variety["fields"]["nf_calories"]

	elif juice_variety["fields"]["nf_serving_size_unit"] == "can":
		fl_oz += 12.0
		calories += juice_variety["fields"]["nf_calories"]

	elif juice_variety["fields"]["nf_serving_size_unit"] == "box":
		fl_oz += 6.75
		calories += juice_variety["fields"]["nf_calories"]
		

text_file = open("item_two.json", "w")
text_file.write("{ \"Avg calories per fl oz\" : " + str(calories / fl_oz) + " }")
text_file.close()
