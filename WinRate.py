import json
import symbols
import prices
import prediction
import results

#Open config.json
f = open("config.json", encoding='utf-8')
#Load config.json
config = json.load(f)
print("Reading Symbols")
symbol_list = symbols.get_list(config)
print(str(len(symbol_list)) + " Files Found")

#Create ValidationFile.csv File
print("Create Result File")
results.create(config)

steps = 0
resultlist = prediction.create_resultlist(config)
while True:
    steps += 1
    print("Saving Prices File……")
    validationList = prices.save_prices_file(config, symbol_list)
    print("Start Prediction……")
    resultlist = prediction.calculate_winrate(config, validationList, resultlist, steps)
    results.append(config, resultlist)
    print("Step " + steps + " Finished.")
