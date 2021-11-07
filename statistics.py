import csv
from collections import Counter

with open('HeightWeight.csv',newline='') as file:
    reader = csv.reader(file)
    fileData = list(reader)

fileData.pop(0)
newData = []

for i in range(len(fileData)):
    n = fileData[i][1]
    newData.append(float(n))

l = len(newData)

def mean(): 
    sum = 0
    for j in newData:
        sum += j
    mean = sum/l
    print('Mean is ' + str(mean))

def median(): 
    newData.sort()
    if l % 2 == 0:
        median1 = float(newData[l//2])
        median2 = float(newData[l//2-1])
        median = (median1 + median2)/2
    else:
        median = newData[l//2]
    print('Median is ' + str(median))

def mode():
    data = Counter(newData)
    mode_data_range = {
    '50-60':0,
    '60-70':0,
    '70-80':0}

    for height, occurrence in data.items():
        if 50 < float(height) < 60 :
            mode_data_range['50-60'] += occurrence
        elif 60 < float(height) < 70 :
            mode_data_range['60-70'] += occurrence
        elif 70 < float(height) < 80 :
            mode_data_range['70-80'] += occurrence

    mode_range, mode_occurrence = 0,0

    for range, occurrence in mode_data_range.items():
        if occurrence > mode_occurrence:
            mode_range, mode_occurrence = [int(range.split('-')[0]),int(range.split('-')[1])],occurrence

    mode = float((mode_range[0] + mode_range[1])/2)
    print('Mode is ' + str(mode))

def main():
    mean()
    median()
    mode()

main()

