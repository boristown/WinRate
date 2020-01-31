import glob
import time
import csv

def calculate_winrate_fromfile(config, validationList, steps, prediction_file):
    resultlist = [] #"Steps","Total","Win","Loss","WinRate"
    with open(prediction_file,"r") as fcsv:
        csvreader = csv.reader(fcsv)
        prices_batch_size = len(validationList)
        predict_index = 0
        time.sleep(5)
        resultlist.append(steps) #0 Steps
        resultlist.append(steps*config["batch"]) #1 Total
        resultlist.append(0) #2 Win
        resultlist.append(0) #3 Loss
        resultlist.append(0.0) #4 WinRate
        for row in csvreader:
            riseflag = 1 if (float)(row[1]) >= 0.5 else 0
            if riseflag == validationList[predict_index]:
                resultlist[2] += 1 #2 Win
            else:
                resultlist[3] += 1 #3 Loss
            predict_index += 1
            if predict_index >= prices_batch_size:
                break
        resultlist[4] = resultlist[2] / prices_batch_size #4 WinRate
    return resultlist

def calculate_winrate(config, validationData, steps):
    # Predict
    while True:
        time.sleep(1)
        predict_files  = glob.glob(config["PredictionFiles"])
        if len(predict_files) == 0:
            continue
        print("Reading Prediction Result……", predict_files[0])
        time.sleep(2)
        resultlist = calculate_winrate_fromfile(validationData, steps, predict_files[0])
        break
    return resultlist
