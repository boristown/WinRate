import glob
import json

f = open("config.json", encoding='utf-8')
config = json.load(f)
print(config)
pricesPath = glob.glob(config["PricesFiles"])
print(pricesPath)
validationFile = open(config["ValidationFile"],'w')
