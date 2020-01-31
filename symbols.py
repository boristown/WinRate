import glob

def get_list(config):
    #Glob Prices Files 
    symbolPath = glob.glob(config["SymbolFiles"])
    symbol_list = []
    #Read Prices Files
    for fileIndex, pricePath in enumerate(symbolPath):
        with open(pricePath) as priceFile:
            price_lines = priceFile.read().splitlines()
            price_list = list(map(float, price_lines))
            symbol_list.append(price_list)
    return symbol_list