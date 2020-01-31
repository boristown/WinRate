import csv

def create(config):
    with open(config["WinRateFile"],"w",newline='') as winrateFile:
        winrateWriter = csv.writer(winrateFile)
        #Write Header
        winrateWriter.writerow(["Steps","Total","Win","Loss","WinRate","Score"])

def append(config, resultline):
    with open(config["WinRateFile"],"a",newline='') as winrateFile:
        winrateWriter = csv.writer(winrateFile)
        winrateWriter.writerow(resultline)