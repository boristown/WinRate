import csv

def create(config):
    with open(config["WinRateFile"],"w",newline='') as winrateFile:
        winrateWriter = csv.writer(winrateFile)
        #Write Header
        winrateWriter.writerow(["Steps",
                                "Total","Total0","Total10","Total20","Total30","Total40","Total50","Total60","Total70","Total80","Total90",
                                "Win","Win0","Win10","Win20","Win30","Win40","Win50","Win60","Win70","Win80","Win90",
                                "WinRate","WinRate0","WinRate10","WinRate20","WinRate30","WinRate40","WinRate50","WinRate60","WinRate70","WinRate80","WinRate90"])

def append(config, resultline):
    with open(config["WinRateFile"],"a",newline='') as winrateFile:
        winrateWriter = csv.writer(winrateFile)
        winrateWriter.writerow(resultline)