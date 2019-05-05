#! python3

import requests
import json
import math


#requesting data from Nutritionix:
urlstr = "https://api.nutritionix.com/v1_1/search"

parameters1 = {
	"appId" : "7492aac4" , 
	"appKey" : "8ec745a2f00c639c7412ba346cc1fcb8" , 
	"brand_id" : "51db37d0176fe9790a899db2"
	}

response1 = requests.get(url = urlstr , params = parameters1)

# Loading JSON structure:
total_data = response1.json()

# Finding out the number of results:
total_hits = total_data["total_hits"]

# You can only request 50 records at a time.  Therefore if the total_hits is greater than 50,
# you have to loop your GET requests:
data = ""

if (total_hits > 50 ):
	num_requests = math.ceil(total_hits / 50)

	for x in range(num_requests):

		results_str = str(50 * x) + ":" + str(50 * (x+1))

		parameters = {
			"appId" : "7492aac4" , 
			"appKey" : "8ec745a2f00c639c7412ba346cc1fcb8" , 
			"results" : results_str , 
			"fields" : "*" ,
			"brand_id" : "51db37d0176fe9790a899db2"
			}

		response = requests.get(url = urlstr, params = parameters)
		
		# The data arrives in json format, but also in chunks, so string it and concatenate:
		data += str(response.json())
		
	# There will be several instances of the opening tags, remove them
	# and replace them with commas:
	replacestr = "]}{'total_hits': " + str(total_hits) + ", 'max_score': 1, 'hits': ["
	datastrtmp = data.replace(replacestr,",")

	# Replace all single quotes with double quotes in preparation for json loading:
	datastrtmp2 = datastrtmp.replace("'","\"")
	
	# Replace all instances of None with "None":
	datastr = datastrtmp2.replace("None","\"None\"")

else:
	# if there are 50 or fewer hits:
	parameters = {
		"appId" : "7492aac4" , 
		"appKey" : "8ec745a2f00c639c7412ba346cc1fcb8" , 
		"results" : "0:50" ,
		"fields" : "item_name,nf_calories,nf_serving_size_qty,nf_serving_size_unit" ,
		"brand_id" : "51db37d0176fe9790a899db2"
		}

	response = requests.get(url = urlstr, params = parameters)
	
	datastr = response

	# Replace all single quotes with double quotes in preparation for json loading:
	datastrtmp2 = datastrtmp.replace("'","\"")
	
	# Replace all instances of None with "None":
	datastr = datastrtmp2.replace("None","\"None\"")


text_file = open("juices.json", "w")
text_file.write(datastr)
text_file.close()
