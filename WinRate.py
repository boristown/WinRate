import glob
import json
import csv

#Open config.json
f = open("config.json", encoding='utf-8')
#Read config.json
config = json.load(f)
print(config)
#Load Prices Files 
pricesPath = glob.glob(config["PricesFiles"])
print(pricesPath)
#Create ValidationFile.csv File
with open(config["ValidationFile"],"w") as validationFile:
    writer = csv.writer(validationFile)
    writer.writerow(["Steps","Total","Win","Loss","WinRate"])
    