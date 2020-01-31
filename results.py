import csv

def create(config):
    with open(config["WinRateFile"],"w") as winrateFile:
        winrateWriter = csv.writer(winrateFile)
        #Write Header
        winrateWriter.writerow(["Steps","Total","Win","Loss","WinRate"])

def append(config, resultline):
    with open(config["WinRateFile"],"a") as winrateFile:
        winrateWriter = csv.writer(winrateFile)
        winrateWriter.writerow(resultline)