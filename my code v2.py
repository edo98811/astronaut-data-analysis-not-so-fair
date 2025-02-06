
import datetime as dt
import csv
import matplotlib.pyplot as plt
import json
import pandas as pd


# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open("data.json", 'r')
output_file = open('/home/sarah/Projects/ssi-ukrn-fair-course/data.csv','w')
graph_file = 'myplot.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data_table=[]

for i in range(374):
    line=input_file.readline()
    print(line)
    data_table.append(json.loads(line[1:-1]))
    
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet

w=csv.writer(output_file)

time = []
date =[]

j=0
for i in data_table:
    print(data_table[j])
    # and this bit
    w.writerow(data_table[j].values())
    if 'duration' in data_table[j].keys():
        tt=data_table[j]['duration']
        if tt == '':
            pass
        else:
            t=dt.datetime.strptime(tt,'%H:%M')
            ttt = dt.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds()/(60*60)
            print(t,ttt)
            time.append(ttt)
            if 'date' in data_table[j].keys():
                date.append(dt.datetime.strptime(data_table[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

t=[0]
for i in time:
    t.append(t[-1]+i)

date,time = zip(*sorted(zip(date, time)))


# Plotting the results 
plt.plot(date,t[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
