import csv
import math

with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    n=len(data)
    total=0

    for i in data:
        total+=int(i)
    
    mean=total/n
    return mean

squared_list=[]

for a in data:
    sub_num=int(a)- mean(data)
    d=sub_num**2
    squared_list.append(d)

sum=0
for c in squared_list:
    sum+=c

result=sum/(len(data)-1)
standar_deviation=math.sqrt(result)
print(standar_deviation)