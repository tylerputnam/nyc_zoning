
'''
DATA we need:
------------------------------------------------
ZONING
------------------------------------------------
is it possible to get data on whether building has water tower, if water tower (or other mechanical equipment) has been removed
Building Height
Zoning Height
Air rights
Air rights Height
OSR (open space ratio)
Building set backs (Height factor districis is controlled by sky exposure planes, in contextual districts by specified distances from street walls)
SETBACKS (maybe we dont need this since this is not new construction)
LotCoverage
LotDepth
LotWidth
LotArea
BuildingFootprint area
	We can get the associated shape file, and maybe append the area to the dataset
Buildable Zoning Height?
FAR
def GetPermittedFAR(zoning):
	if zoning == 'r8'
		return PermittedFAR = 0.6
	if zoning == 'r9'
		return PermittedFAR = 0.7
GrossFloorArea
ActualFAR = GrossFloorArea / LotArea
UnusedFAR = ActualFAR - PermittedFAR
UnusedSQFT = UnusedFAR * LotArea

Price per SQFT = Valuation of the entire building / PPSQFT

Maximum permitted Floor Area
actual built Floor Area
Unused Development Rights
Condo -- TaxLot
Co-Op -- TaxLot

Landmark Building
Landmark Interior
Historic District
Scenic Landmark District




Sources of DATA Include:
ACRIS -
	What data do they have?
	Will Have to be mined
	API Limits?
NYC.GOV
	DOB-
		Borough Code,Tax Block,Tax Lot,Zoning District 1,Zoning District 2,Zoning District 3,Zoning District 4,Commercial Overlay 1,Commercial Overlay 2,Special District 1,Special District 2,Limited Height District,Zoning Map Number,Zoning Map Code
	DOF-
		Property Valuation and assessment Data Tax class
			Boundaries (boundaries are identified by Hook symbols):
				REUC
				Easement
		http://www1.nyc.gov/assets/finance/downloads/pdf/rolling_sales/rollingsales_manhattan.pdf
			Sale Price of last year
			land square feet
			gross square feet
			building class
			apartment number
			Building class category
Real estate database -
	What Data do they have that would be useful?
Will Have to be mined
	API Limits?
http://furmancenter.org/data
	TDR and other transfer rights
------------------------------------------------------------------------------------------------------------------------------------

Ultimate Goal -
	return properties that have enough FAR with highest value per sqft.

Sort data by highest index
	'''

Lots == Take a data set of all New York City Lots.
BoroughLots == Lots[‘boroughcode’] = 1 or 2 or 3
ResiLots == Lots[‘residential’] Filter this data set by residential zoned buildings.
split data set into:
Lots[FAR] == FAR of the lot (should be able to get this from one of the databases)
Lots[‘FAR.MAX’] will need air rights transferred over
Lots[‘PPSQFT’] == typical apartment price / sqft of apartment
FARSQFT_Price_Ratio == Lots[FAR] * lots[‘PPSQFT’]
return Lots[‘FAR’]<FARSQFT_Price_Ratio = which is not maxed out -- above X sqft left over

RoofSQFT
Buildable RoofSQFT = RoofSQFT - set backs, if [‘landmarks’] == true then subtract view shed

RoofPPSQFT == top floor apartmentPPSQFT / 2


