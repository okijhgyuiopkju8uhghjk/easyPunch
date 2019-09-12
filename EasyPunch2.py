from datetime import datetime
import random

noOfDayInMonth = 31

clsNsun =[1,2,4,11,18,25]
dutydays =[3,12,16,26,29]
dOffs = [5,13,17,27,30]

# ___________________________________________________
present = []
inTime = []
outTime = []
hours = []

for i in range(0,noOfDayInMonth):
    present.append("P")

for i in clsNsun + dOffs:
    present[i-1] = "A"

for x in range(0, noOfDayInMonth):
    i = random.randint(8, 9)
    if i == 8:
        tim2 = random.randint(45, 59)
    else:
        tim2 = random.randint(1, 15)
    timein = str(i) + ":" + str(tim2)

    inTime.append(timein)

for i in clsNsun:
    inTime[i-1] = "00:00"

for x in range(0, noOfDayInMonth):
    out = random.randint(30, 59)
    timeOut = str(15) + ":" + str(out)

    outTime.append(timeOut)

for i in clsNsun:
    outTime[i-1] = "00:00"

for x in range(0, noOfDayInMonth):
    FMT = '%H:%M'
    hr = datetime.strptime(outTime[x], FMT) - datetime.strptime(inTime[x], FMT)

    hours.append(str(hr))

for i in dutydays:
    outTime[i-1] = "00:00"
    hours[i-1] = "00:00:00"

for n, i in enumerate(inTime):
    if i == "00:00":
        inTime[n] = ""
for n, i in enumerate(outTime):
    if i == "00:00":
        outTime[n] = ""
for n, i in enumerate(hours):
    if i == "0:00:00":
        hours[n] = "00:00:00"

for i in dOffs:
    present[i-1] = "A"
    outTime[i-1] = ""
    hours[i-1] = "00:00:00"

newhours = [x[:-3] for x in hours]
# ___________________________________________________________
print(*present,sep="\t")
print(*inTime ,sep="\t")
print(*outTime,sep="\t")
print(*newhours,sep="\t")
