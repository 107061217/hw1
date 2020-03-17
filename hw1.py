# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = 'sample_input.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:
      data.append(row)    # put row into data
   
#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

target_data = list(filter(lambda item: (item['station_id'] == 'C0A880' or item['station_id'] == 'C0F9A0' or item['station_id'] == 'C0G640' or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260'), data))

# Retrive ten data points from the beginning.

# target_data = data[:10]


#=======================================


# Part. 4

#=======================================

# Print result

n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
sum = 0.0
SP_A880 = 0.0
SP_F9A0 = 0.0
SP_G640 = 0.0
SP_R190 = 0.0
SP_X260 = 0.0

for i in range(len(target_data)):
   if (target_data[i]['station_id'] == 'C0A880') :
      if (target_data[i]['HUMD'] == '-99.000' or target_data[i]['HUMD'] == '-999.000') :
         SP_A880 = SP_A880
      else :
         SP_A880 = SP_A880 + float(target_data[i]['HUMD'])
   elif (target_data[i]['station_id'] == 'C0F9A0') :
      if (target_data[i]['HUMD'] == '-99.000' or target_data[i]['HUMD'] == '-999.000') :
         SP_F9A0 = SP_F9A0
      else :
         SP_F9A0 = SP_F9A0 + float(target_data[i]['HUMD'])
   elif (target_data[i]['station_id'] == 'C0G640') :
      if (target_data[i]['HUMD'] == '-99.000' or target_data[i]['HUMD'] == '-999.000') :
         SP_G640 = SP_G640
      else :
         SP_G640 = SP_G640 + float(target_data[i]['HUMD'])
   elif (target_data[i]['station_id'] == 'C0R190') :
      if (target_data[i]['HUMD'] == '-99.000' or target_data[i]['HUMD'] == '-999.000') :
         SP_R190 = SP_R190
      else :
         SP_R190 = SP_R190 + float(target_data[i]['HUMD'])
   elif (target_data[i]['station_id'] == 'C0X260') :
      if (target_data[i]['HUMD'] == '-99.000' or target_data[i]['HUMD'] == '-999.000') :
         SP_X260 = SP_X260
      else :
         SP_X260 = SP_X260 + float(target_data[i]['HUMD'])

if (SP_A880 == 0) :
   val_A880 = str(None)
else :
   val_A880 = str(format(SP_A880, '.2f'))
if (SP_F9A0 == 0) :
   val_F9A0 = str(None)
else :
   val_F9A0 = str(format(SP_F9A0, '.2f'))
if (SP_G640 == 0) :
   val_G640 = str(None)
else :
   val_G640 = str(format(SP_G640, '.2f'))
if (SP_R190 == 0) :
   val_R190 = str(None)
else :
   val_R190 = str(format(SP_R190, '.2f'))
if (SP_X260 == 0) :
   val_X260 = str(None)
else :
   val_X260 = str(format(SP_X260, '.2f'))


print('''[['C0A880',''', val_A880 + '],', '''['C0F9A0',''', val_F9A0 + '],', '''['C0G640',''', val_G640 + '],', '''['C0R190',''', val_R190 + '],', '''['C0X260',''', val_X260 + ']]')   

#print("['C0R190', ", target_data[2]['HUMD'], "]")

#========================================