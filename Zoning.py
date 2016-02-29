#####################################################
##### FIrst attempt at an algorithm for NYC's RoofTop Additions
#####AUTHOR: T.Lord
##Two Hashes = stuff to update
# One Hash = is just a note on what the code does

##Make iPython Notebook out of this code
## Numpy, SCipy Etc.
##Connect github and ipython
##import panda and put ZoneTax into a dataframe
##import Sea and visualize the data via graph

##add exception handling to all datafields

##Need to get ZoneTax into actual Useable Dictionary Data
##Figure out what to do about the 4 different zoning designations
##Special Districts
##limited Height Districts --- Probably just filter these out
#####################################################
import os
import math
from random import randint
import sys
import numpy as np
import scipy
import pylab
import sympy
import pytest
import pandas as pd
import seaborn as sns
# %matplotlib inline # IPython magic to create plots within cells
import csv
#####################################################
ZoneTax = csv.DictReader(open('NYC_ZoningTaxLotDB_201601.csv'))
#####################################################
# ##Dummy DataSet need to add real dataSet
# Lots = [
# 	{'Zoning District 1': 'R4B', 'Borough Code' : '1','Tax Block':'3','Tax Lot':'3'},
# 	{'Zoning District 1': 'R7-3', 'Borough Code' : '2','Tax Block':'5','Tax Lot':'4'},
# 	{'Zoning District 1': 'R4A', 'Borough Code' : '3','Tax Block':'6','Tax Lot':'5'},
# 	{'Zoning District 1': 'C9', 'Borough Code' : '4','Tax Block':'5','Tax Lot':'3'}
# 	]
#####################################################
#####################################################
#New DICT per borough
Mn = [row for row in ZoneTax if row['Borough Code'] == '1']
Bx = [row for row in ZoneTax if row['Borough Code'] == '2']
Bk = [row for row in ZoneTax if row['Borough Code'] == '3']
Qu = [row for row in ZoneTax if row['Borough Code'] == '4']
Si = [row for row in ZoneTax if row['Borough Code'] == '5']
# print(Mn)
Lots = Mn




df = pd.DataFrame(Lots)
df1 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D' : pd.Series([1, 2, 1, 2], dtype='int32'),
                    'E' : pd.Categorical(["test", "train", "test", "train"]),
                    'F' : 'foo' })
print df
print df1



####################################################
#VARIABLES WE HAVE NOT GOT YET
####################################################

for x in Lots:
	x['GrossFloorArea'] = randint(1000,10000)
	x['LotArea'] = randint(1000,5000)
	x['AssesmentValue'] = randint(100000,200000)

####################################################

#Filters Dataset into Residential datasets.
##Sloppy filtering -- adds new dict would be better to call a function
##must add all residential filters to this
# need to add exclusion for 'Sk# NEED TO REPLACE WITH  Exposure Plane' in Calculations'Tower Rules'
# need to add exclusion for 350 in Calculations
# This is Limiting us to just 4 properties....2:11 Feb 29/2016
ResiLots = [x for x in Lots if
	( 'R7-3' == x.get('Zoning District 1'))or
	( 'R3-2' == x.get('Zoning District 1')) or
	('R1-1' == x.get('Zoning District 1')) or
	('R1-2' == x.get('Zoning District 1')) or
	('R2' == x.get('Zoning District 1')) or
	('R2A' == x.get('Zoning District 1')) or
	('R2X' == x.get('Zoning District 1')) or
	('R3A' == x.get('Zoning District 1')) or
	('R3X' == x.get('Zoning District 1')) or
	('R3-1' == x.get('Zoning District 1')) or
	('R3-2' == x.get('Zoning District 1')) or

	('R4' == x.get('Zoning District 1')) or

	('R4-1' == x.get('Zoning District 1')) or

	('R4A' == x.get('Zoning District 1')) or
	('R4B' == x.get('Zoning District 1')) or


	('R4/R5 Infill' == x.get('Zoning District 1')) or
	('R5' == x.get('Zoning District 1')) or
	('R5A' == x.get('Zoning District 1')) or
	('R5B' == x.get('Zoning District 1')) or
	('R5D' == x.get('Zoning District 1')) or
	('R6HF' == x.get('Zoning District 1')) or
	('R6HQ' == x.get('Zoning District 1')) or

	('R6A' == x.get('Zoning District 1')) or
	('R6B' == x.get('Zoning District 1')) or
	('R7HF' == x.get('Zoning District 1')) or
	('R7QH' == x.get('Zoning District 1')) or
	('R7-3' == x.get('Zoning District 1')) or
	('R7A' == x.get('Zoning District 1')) or
	('R7B' == x.get('Zoning District 1')) or
	('R7D' == x.get('Zoning District 1')) or
	('R7X' == x.get('Zoning District 1')) or

	('R8HF' == x.get('Zoning District 1')) or
	('R8QH' == x.get('Zoning District 1')) or
	('R8A' == x.get('Zoning District 1')) or
	('R8B' == x.get('Zoning District 1')) or
	('R8X' == x.get('Zoning District 1')) or
	('R89HF' == x.get('Zoning District 1')) or
	('R8QH' == x.get('Zoning District 1')) or
	('R9A' == x.get('Zoning District 1')) or
	('R9-1' == x.get('Zoning District 1')) or
	('R9X' == x.get('Zoning District 1')) or
	('R910' == x.get('Zoning District 1')) or
	('R10QH' == x.get('Zoning District 1')) or
	('R10A' == x.get('Zoning District 1')) or
	('R10X' == x.get('Zoning District 1'))
	]
##############################################################

##need to add all the rest of the FAR permitted values here
#units in Feet
# Exludes lot coverage max etc.

# need to add exclusion for 'Sk# NEED TO REPLACE WITH  Exposure Plane' in Calculations'Tower Rules'
# need to add exclusion for 350 in Calculations
## Probaly need to convert this to try:

def GetPermittedFAR(x):
	if x['Zoning District 1'] == 'R1-1':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R1-2':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R2':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R2A':
		x['Building Height Max'] = 35
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R2X':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R3A':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R3X':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R3-1':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R3-2':
		x['FAR_Permitted'] = 0.5
		x['Building Height Max'] = 35
#--------------Lower Density Housing ---------------------
	if x['Zoning District 1'] == 'R4':
		x['FAR_Permitted'] = 0.75
		x['Building Height Max'] = 35
	#Check for nomenclature
	if x['Zoning District 1'] == 'R4-1':
		x['FAR_Permitted'] = 0.75
		x['Building Height Max'] = 35
	#Check for nomenclature
	if x['Zoning District 1'] == 'R4A':
		x['FAR_Permitted'] = 0.75
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R4B':
		x['FAR_Permitted'] = 0.9
		x['Building Height Max'] = 24
	#Check for nomenclature
	#far permitted is not actually defined
	if x['Zoning District 1'] == 'R4/R5':
		x['FAR_Permitted'] = 1.45
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R5':
		x['FAR_Permitted'] = 1.25
		x['Building Height Max'] = 40
	if x['Zoning District 1'] == 'R5A':
		x['FAR_Permitted'] = 1.1
		x['Building Height Max'] = 35
	if x['Zoning District 1'] == 'R5B':
		x['FAR_Permitted'] = 1.35
		x['Building Height Max'] = 33
	if x['Zoning District 1'] == 'R5D':
		x['FAR_Permitted'] = 2.0
		x['Building Height Max'] = 40
#--------------Medium Density Housing ---------------------
	if x['Zoning District 1'] == 'R6HF':
# RANGE of FAR 0.78 -- 2.43
#' NEEDS TO BE REPLACED WITH 0
		x['FAR_Permitted'] = 1
# NEED TO REPLACE 'Sky Exposure Plane'
		x['Building Height Max'] = 350
	if x['Zoning District 1'] == 'R6HQ':
	#' NEEDS TO BE REPLACED WITH 1
		x['FAR_Permitted'] = 1
#Narrow to wide 55-75
		x['Building Height Max'] = 70
	if x['Zoning District 1'] == 'R6A':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 75
	if x['Zoning District 1'] == 'R6B':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 50
	if x['Zoning District 1'] == 'R7HF':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
# NEED TO REPLACE 'Sky Exposure Plane'
		x['Building Height Max'] = 350
	if x['Zoning District 1'] == 'R7QH':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Narrow to wide 75-80
		x['Building Height Max'] = 75
#Check for nomenclature
	if x['Zoning District 1'] == 'R7-3':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 185
	if x['Zoning District 1'] == 'R7A':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 80
	if x['Zoning District 1'] == 'R7B':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 75
	if x['Zoning District 1'] == 'R7D':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 100
	if x['Zoning District 1'] == 'R7X':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 125

#Higher Density Residence Districts
	if x['Zoning District 1'] == 'R8HF':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
# NEED TO REPLACE 'Sky Exposure Plane'
		x['Building Height Max'] = 350
	if x['Zoning District 1'] == 'R8QH':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Narrow to wide 120 to 105
		x['Building Height Max'] = 100
	if x['Zoning District 1'] == 'R8A':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 120
	if x['Zoning District 1'] == 'R8B':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 75
	if x['Zoning District 1'] == 'R8X':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 150
	if x['Zoning District 1'] == 'R8HF':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
# or tower Rules
# NEED TO REPLACE 'Sky Exposure Plane'
		x['Building Height Max'] = 350
#Check for nomenclature
	if x['Zoning District 1'] == 'R8QH':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Narrow to wide 145 to 135
		x['Building Height Max'] = 140
	if x['Zoning District 1'] == 'R9A':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
		x['Building Height Max'] = 140
#Check for nomenclature
	if x['Zoning District 1'] == 'R9-1':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Check for nomenclature
		x['Building Height Max'] = 140
	if x['Zoning District 1'] == 'R9X':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Narrow to wide 170 t0 160
		x['Building Height Max'] = 160
	if x['Zoning District 1'] == 'R910':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
# NEED TO REPLACE WITH 'Tower Rules'
		x['Building Height Max'] = 350
	if x['Zoning District 1'] == 'R10QH':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Narrow to wide 210 to 185
		x['Building Height Max'] = 200
	if x['Zoning District 1'] == 'R10A':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
#Narrow to wide 210 to 185
		x['Building Height Max'] = 200
	if x['Zoning District 1'] == 'R10X':
# 1 needs to be repaced w/ ' '
		x['FAR_Permitted'] = 1
# NEED TO REPLACE WITH 'Tower Rules'
		x['Building Height Max'] = 350




##Make a new field in the data base which is the BBL.
#This will be useful when Concatenating this data with other databases
#4/99999/9999
# We are going to have to make this fuzzy enough for other databases because of the decimal places
def getBBL(x):
	x['BBL'] = ''.join([x['Borough Code'], '/', x['Tax Block'], '/', x['Tax Lot']])
#This figure is currently unrealistic because it does not subtract out Cores / Hallways / a bunch of other sqft
#Either we get actual figures from Database or we use some statistical modeling to approximate this


def getFAR(x):
	x['FAR'] = x['GrossFloorArea'] / x['LotArea']
	x['FAR_Unused'] = x['FAR'] - x['FAR_Permitted']
	x['UnusedSQFT'] = x['FAR_Unused'] * x['LotArea']
##############################################################
def getPpSQFT(x):
	x['PpSQFT']  =x['AssesmentValue'] / x['GrossFloorArea']

## Likely to be other factors involved here
def getRoof_PpSQFT(x):
	x['Roof_PpSQFT'] = x['PpSQFT'] / 2

##Add FAR_Permitted to dict
[x for x in ResiLots if GetPermittedFAR(x)]
#add to list comprehension above
for x in ResiLots:
	getBBL(x)
	getFAR(x)
	getPpSQFT(x)
	getRoof_PpSQFT(x)

# print(ResiLots)
# print("The Number of Units Filtered is :" )
# print( len(ResiLots))



