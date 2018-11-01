import csv 
import json



infile = open("twitter_json.json","r")
outfile = open("twitter_info.csv","a")
header = ["screen_name","text","created at","url","indicies", "lang"]

source_file = open(“twitter_json.json”,“r”);
#json_data = json.load(source_file)
json_data = json.load(source_file)
json_dict = json.loads(json_data

info = {"created at" : "Fri Apr 06 05:13:44 +0000 2018", "screen_name" : "BoudlHotels","text" : "RT @BoudlHotels:"
,"indicies":"[3, 15]"
,"url":"[]"
,"lang":"ar"
}

writer = csv.writer(outfile)
writer.writerow(header)
for row in json.loads(infile.read()):
	writer.writerow(row)
key_names = info.keys()
key_names = [info[i] for i in key_names]
for i in info.keys():
		writer.writerow(key_names)
