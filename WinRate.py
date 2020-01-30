import glob
import json
import csv
import random
import prices
import datetime
import os

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

#Delete Old Price Files
prices_files  = glob.glob(config["Output_prices_file"])
for prices_file in prices_files:
    os.remove(prices_file)

#Delete Old Predict Files
predict_files  = glob.glob(config["Output_predict_file"])
for predict_file in predict_files:
    os.remove(predict_file)

time.sleep(1)

time_text =  datetime.datetime.utcnow().strftime("%Y%m%d")
price_filename_txt = os.path.join(config["Output_prices_prefix"] + 'part-WinRate_' + time_text + '.txt')
price_filename_csv = os.path.join(config["Output_prices_prefix"] + 'price-WinRate_' + time_text + '.csv')
price_file = open(price_filename_txt, "w", encoding="utf-8")
price_file.truncate()

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
    price_file.write(','.join(list(map(str,trainingDataElement))) + '\n')
#Save prices.csv
price_file.close()
os.rename(price_filename_txt, price_filename_csv)

print("Start Prediction……")



#Create ValidationFile.csv File
with open(config["ValidationFile"],"w") as validationFile:
    writer = csv.writer(validationFile)
    writer.writerow(["Steps","Total","Win","Loss","WinRate"])
    