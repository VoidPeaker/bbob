import random, os, json, time, math, pandas as pd
#from convertexcel import loadResources, resourcesPath

resourcesPath = "./bbob/resources/"


def convertExcelSheetIntoJson(sheetName):
    file = open(sheetName+".json", "w")
    hold = pd.read_excel(resourcesPath + "elements.xlsx",sheet_name=sheetName,index_col=0)
    file.write(hold.to_json())
    file.close()
    return json.load(sheetName+".json")


convertExcelSheetIntoJson("adjectives")