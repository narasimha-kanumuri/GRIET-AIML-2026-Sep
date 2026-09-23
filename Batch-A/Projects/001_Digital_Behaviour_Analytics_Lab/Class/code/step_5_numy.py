import numpy as np
import csv

insta_minutes = []
study_minutes = []

with open("./digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row["Instagram_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))

insta_minutes=insta_minutes[:7]
study_minutes=study_minutes[:7]

instagram = np.array(insta_minutes)
study = np.array(study_minutes)

print(instagram, study)

#total = np.sum(instagram)
total = instagram.sum()
average = instagram.mean()
maximum = instagram.max()
minimum = instagram.min()
days = len(instagram)

s_total = study.sum()
s_average = study.mean()
s_maximum = study.max()
s_minimum = study.min()
s_days = len(study)

print(f"Toal {total}, Average {average}, Maximum {maximum}, Minimum {minimum}, Days {days}")

print(instagram[0], instagram[-1], instagram[2])

print(instagram[:3], instagram[-2:], instagram[1:4], instagram[::2])

i_hours = instagram/60

#i_hours = np.round(i_hours, 2)
i_hours = i_hours.round(2)

difference = study - instagram

'''greater = [val for val in difference if val > 100]

for val in difference:
    if val > 100:
        greater.append(val)'''

#boolean = instagram>100
#print(greater)
#greater = [bool_ for bool_ in boolean if bool_]
#greater = filter(lambda bool_: bool_, boolean)

#greater = instagram[boolean]
[20,125, 30, 150, 40, 200, 50]
greater = instagram[instagram>100]

'''count = (instagram>100)
count = count.sum()'''
count = (instagram>100).sum()

value = instagram[instagram>average]

