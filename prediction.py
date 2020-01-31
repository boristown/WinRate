import glob
import time
import csv
import math

def create_resultlist(config):
    resultlist = []
    for i in range(21):
        resultlist.append(0) #Steps,Total,Win
    for i in range(10):
        resultlist.append(0.0) #WinRate
    return resultlist

def calculate_winrate_fromfile(config, validationList, steps, resultlist, prediction_file):
    with open(prediction_file,"r") as fcsv:
        csvreader = csv.reader(fcsv)
        prices_batch_size = len(validationList)
        predict_index = 0
        time.sleep(5)
        resultlist[0] += 1 #0 Steps
        resultlist[1] += config["batch"] #1 Total
        for row in csvreader:
            predictValue = (float)(row[1])
            predictScoreIndex = math.floor(abs((float)(row[1]) * 2 - 1) * 10.0)
            resultlist[predictScoreIndex + 1] += 1
            riseflag = 1 if predictValue >= 0.5 else 0
            if riseflag == validationList[predict_index]:
                resultlist[predictScoreIndex + 11] += 1 #2 Win
            predict_index += 1
            if predict_index >= prices_batch_size:
                break
        for i in range(10):
            resultlist[i + 21] = resultlist[i + 11] / resultlist[i + 1] if resultlist[i + 1] > 0 else 0.5 #4 WinRate
    return resultlist

def calculate_winrate(config, validationList, resultlist, steps):
    # Predict
    while True:
        time.sleep(1)
        predict_files  = glob.glob(config["PredictionFiles"])
        if len(predict_files) == 0:
            continue
        print("Reading Prediction Result……", predict_files[0])
        time.sleep(2)
        resultlist = calculate_winrate_fromfile(config, validationList, steps, resultlist, predict_files[0])
        break
    return resultlist
