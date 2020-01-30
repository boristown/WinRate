import glob
import json
import csv
import random
import prices

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

trainingData = []
validationData = []
for trainingIndex in range(config["batch"]):
    #Generate Random Number
    randomSymbolIndex = random.randint(0, len(symbol_list)-1)
    randomSymbol = symbol_list[randomSymbolIndex]
    randomPriceIndex = random.randint(config["priceCount"] - 1, len(randomSymbol) - 2)
    trainingDataElement = prices.scale_to_0_1(randomSymbol[randomPriceIndex+1-config["priceCount"]:randomPriceIndex+1:1][-1::-1])
    #Generate Training Data
    trainingData.append(
        trainingDataElement
        )
    validationData.append(
        1 if randomSymbol[randomPriceIndex+1] > randomSymbol[randomPriceIndex] else 0
        )
#Save prices.csv
print(trainingData)

#Create ValidationFile.csv File
with open(config["ValidationFile"],"w") as validationFile:
    writer = csv.writer(validationFile)
    writer.writerow(["Steps","Total","Win","Loss","WinRate"])
    