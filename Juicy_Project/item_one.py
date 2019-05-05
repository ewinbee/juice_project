#! python3

import requests
import json


#requesting data from Nutritionix:
urlstr = "https://api.nutritionix.com/v1_1/search"

parameters = {
	"appId" : "7492aac4" , 
	"appKey" : "8ec745a2f00c639c7412ba346cc1fcb8" , 
	"brand_id" : "51db37d0176fe9790a899db2"
	}

response = requests.get(url = urlstr , params = parameters)

# Loading JSON structure:
total_data = response.json()

# Finding out the number of results:
total_hits = total_data["total_hits"]

# Item #1  The total results in JSON format:
text_file = open("item_one.json", "w")
text_file.write("{ \"total_hits\" : " + str(total_hits) + " }")
text_file.close()
