import numpy as np
import json
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

import sys

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--inputFolder", type=str, required=True, help="Input folder of json files" )
parser.add_argument("--runList", type=str, required=True, help="List all run number from lower angle/voltage to higher; ex. [41,42,43,44]" )
parser.add_argument("--scanType", type=str, required=True, choices=["angle","voltage"], nargs='*',help="Choose between angle or voltage scan" )

args = parser.parse_args()
scanType = args.scanType
runList  = args.runList
inputFolder = args.inputFolder

#function to read json

def getArrays(json_dict):
    mean  = []
    A     = []
    B     = []
    C     = []
    
    keys = np.array([key for key in json_dict.keys()])
    #keys.sort()
    
    #keys = keys[:-1]
    for ch in keys:
        #print(ch)
        fit_param = json_dict[str(ch)]
        #print(limit.keys())
        #print(limit['mean'])
        try:
           mean.append(fit_param['mean'])
           A.append(fit_param['A'])
           B.append(fit_param['B'])
           C.append(fit_param['C'])
        except:
           mean.append(0.0)
           A.append(0.0)
           B.append(0.0)
           C.append(0.0)
           print("Channel empty: ",ch) 
         
    return  mean, A, B, C, keys

mean_array = []
A_array    = []
B_array    = []
C_array    = []

lst = runList[1:-1].split(',')
RunNum =  [int(i) for i in lst]
print(RunNum)

for num in RunNum:
        filename = inputFolder+"/tbdata_"+str(num)+".json"
        with open(filename) as json_file:
            json_dict = json.load(json_file)
            mean, A, B, C, ch = getArrays(json_dict)
            mean_array.append(mean)
            A_array.append(A)
            B_array.append(B)
            C_array.append(C)

print("mean: ",mean_array)
print("A: ", A_array)
print("B: ", B_array)
print("C: ", C_array)

#plots

fig = plt.figure(figsize=(18,12))
axs = fig.subplots(4,4)

for num, chs in enumerate(ch):
   
    print(num)
    Row = int(num / 4)
    Column = num % 4
    print("Row: ", Row)
    print("Col: ",Column)
    ax = axs[Row][Column]

    enum = 0
    y_axis = []
    erry   = []
    for item in RunNum:
         y_axis.append(B_array[enum][num])
         erry.append(C_array[enum][num]/2)
         enum+=1
    if scanType =="voltage":
         x_axis=["HV-10", "HV", "HV+10", "HV+20"]
    else:
         x_axis=["0", "30", "45", "60"]
    print(x_axis)
    print(y_axis)
    print(erry)
    ax.errorbar(x_axis, y_axis,yerr= erry, fmt='o', linewidth=2, capsize=6)
    ax.set_ylabel('MPV amplitude [V]')
    y_axis.clear()
    erry.clear()

    ax.set_title(f"ch {num} ")#, loc=loc)
    #ax.text(0.5, 0.125, f"ch {num} ", fontsize=15)


fig.savefig(str(scanType[0])+"Scan_Run"+str(RunNum[0])+str(RunNum[1])+str(RunNum[2])+str(RunNum[3])+".pdf")

