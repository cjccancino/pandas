import csv
import os
import pandas as pd
from configparser import ConfigParser



parser = ConfigParser()
parser.read('config.ini')
destination_path = parser['general']['destination_folder']
reference = parser['general']['reference_folder']
excelfile = "report.csv"
outputfile = "updatedreport.csv"


def replaceNull():
    try:
        logf = open(os.path.join(destination_path, "error.log"), "w")
        data = pd.read_csv(os.path.join(reference, excelfile))

        data['Address'].fillna("No Address", inplace = True) 
        
        data.to_csv(os.path.join(destination_path, outputfile), header=True, index=False)

    except Exception as err:
        logf.write(str(err.args))

replaceNull()