import glob
import json
import csv

#Open config.json
f = open("config.json", encoding='utf-8')
#Read config.json
config = json.load(f)
print(config)
#Glob Prices Files 
pricesPath = glob.glob(config["PricesFiles"])
print(pricesPath)
symbol_list = []
#Read Prices Files
for fileIndex, pricePath in enumerate(pricesPath):
    with open(pricePath) as priceFile:
        price_lines = priceFile.read().splitlines()
        price_list = list(map(float, price_lines))
        symbol_list.append(price_list)
        print(len(symbol_list))
#Create ValidationFile.csv File
with open(config["ValidationFile"],"w") as validationFile:
    writer = csv.writer(validationFile)
    writer.writerow(["Steps","Total","Win","Loss","WinRate"])
    