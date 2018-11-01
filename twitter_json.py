import json
import csv


#Open JSON file to read

source_file = open(“twitter_json.json”,“r”);
#json_data = json.load(source_file)
json_data = json.load(source_file)
json_dict = json.loads(json_data)


#print(json_data)
print(“This file is of type”,type(json_dict))

#print(json_dict.keys())
print(json_dict[“statuses”][:][0][“entities”][“user_mentions”][0][“scr”])