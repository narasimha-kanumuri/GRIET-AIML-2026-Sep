import csv

APP = "Instagram"

minutes = []

with open("./digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))
minutes = minutes[0:7]

'''s=input()
s[1::2] + s[0::2]'''

total = sum(minutes)

average = total // len(minutes)

highest = max(minutes)

lowest = min(minutes)

count=0
'''for i in range(len(minutes)):
    if minutes[i]>average:
'''        
for value in minutes:
    if value > average:
        count+=1

print(f"App: {APP}, Total Minutes: {total}, Average Minutes: {average}, Highest Minutes: {highest}, Lowest Minutes: {lowest}, Days Above Average: {count}")
#App: Instagram, Total Minutes: 711, Average Minutes: 101, Highest Minutes: 228, Lowest Minutes: 21, Days Above Average: 2