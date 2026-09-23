'''#app name
APP = "Instagram"

minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(row[im])


# minutes[start:stop:step]

minutes[:7]

# ADDITION
total = sum(minutes)

# AVERAGE VALUE
average = total/len(minutes) 

# MAXIMUM VALUE


# MINIMUM VALUE


# COUNT VALUES > A
counter = 0

for i in minutes :
    if i > average :
        counter+= 1

# PRINT THE VALUES

"""PRINT THE APP NAME , TOTAL , AVG , MAX , MIN , COUNTER , 
   IN ONE LINE USING 'f' STRINGS
"""


    



'''

# PROGRAM 1 NUMPY FILE

import numpy as np

insta_list = []

study_time = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(row[APP])
        study_time.append(row["Study Time"])

insta_list = insta_list[:7]
study_time = study_time[:7]

# CONVERT TO NUMPY ARRAYS

insta_array = np.array(insta_list)
study_array = np.array(study_time)

# total = np.sum(insta_array)

total = insta_array.sum()

# average = np.mean(insta_array)
average = insta_array.mean()

#minimum = np.min(insta_array)
minimum = np.min(insta_array)

maximum = np.max(insta_array)





help(insta_array)







  
