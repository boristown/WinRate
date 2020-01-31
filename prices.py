import glob
import random
import numpy as np
import os
import datetime
import time

def scale_to_0_1(lst):
    ndarray = np.array(lst)
    scaled = np.interp(ndarray, (ndarray.min(), ndarray.max()), (0, 1))
    return scaled.tolist()

def save_prices_file(config, symbol_list):
    validationList = []
    #Delete Old Price Files
    prices_files  = glob.glob(config["PricesFiles"])
    for prices_file in prices_files:
        os.remove(prices_file)

    #Delete Old Predict Files
    predict_files  = glob.glob(config["PredictionFiles"])
    for predict_file in predict_files:
        os.remove(predict_file)

    time.sleep(1)

    time_text =  datetime.datetime.utcnow().strftime("%Y%m%d")
    price_filename_txt = os.path.join(config["PricesDirectory"] + 'part-WinRate_' + time_text + '.txt')
    price_filename_csv = os.path.join(config["PricesDirectory"] + 'price-WinRate_' + time_text + '.csv')
    price_file = open(price_filename_txt, "w", encoding="utf-8")
    price_file.truncate()

    for trainingIndex in range(config["batch"]):
        #Generate Random Number
        randomSymbolIndex = random.randint(0, len(symbol_list)-1)
        randomSymbol = symbol_list[randomSymbolIndex]
        randomPriceIndex = random.randint(config["priceCount"] - 1, len(randomSymbol) - 2)
        pricesData = scale_to_0_1(randomSymbol[randomPriceIndex+1-config["priceCount"]:randomPriceIndex+1:1][-1::-1])
        #Generate Validation Data
        validationList.append(
            1 if randomSymbol[randomPriceIndex+1] > randomSymbol[randomPriceIndex] else 0
            )
        price_file.write(','.join(list(map(str,pricesData))) + '\n')
    #Save prices.csv
    price_file.close()
    os.rename(price_filename_txt, price_filename_csv)
    return validationList