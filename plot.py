#!/usr/bin/python3
from matplotlib import pyplot as plt
from datetime import datetime
import sys

inputFile = sys.argv[1]
x = []          #time
y1 = []         #500s
y2 = []         #200s
y3 = []         #404s
allVals = []    #list of lists
with open(inputFile) as f:
    counter = 0
    for line in f:
        line = line.rstrip()
        values = line.split("\t")
        intList = [int(i) for i in values]
        allVals.append(intList) #all lists are here 

        if counter >= 6:
            timeObject = datetime.fromtimestamp(allVals[counter][0])
            x.append(timeObject.strftime("%H:%M:%S"))
            y1.append(int((allVals[counter][1] - allVals[counter - 6][1])/60))
            y2.append(int((allVals[counter][2] - allVals[counter - 6][2])/60))
            y3.append(int((allVals[counter][3] - allVals[counter - 6][3])/60))
        
        counter += 1

fig, ax = plt.subplots()
plt.plot(x, y1, label="500s")
plt.plot(x, y2, label = "200s")
plt.plot(x, y3, label = "404s")

numTicks = 60
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % numTicks != 0:
        label.set_visible(False)

plt.legend()
plt.xlabel('Time', fontsize = 16)
plt.ylabel('RPS (1-Minute Rate', fontsize = 16)
plt.title('Website Monitoring Rate Graph', fontsize = 26)
plt.savefig('WebsiteMonitoringRatePlot.png')
plt.show()