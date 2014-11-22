-- RENTAL/OWNERSHIP STATUS
-- Universe: Occupied Housing Units
-- Table: H14
-- Attributes: Owner-Occupied H0140002
--			   Renter-Occupied H0140010

\copy (select s.logrecno, sum(h0140002) from sf1_00044 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' group by s.logrecno order by s.logrecno desc) to 'ownerOccupied2.csv' with delimiter ',' csv header;

\copy (select s.logrecno, sum(h0140010) from sf1_00044 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' group by s.logrecno order by s.logrecno desc) to 'renterOccupied2.csv' with delimiter ',' csv header;

-- VACANT HOUSING UNITS
-- Universe: Vacant Housing Units
-- Table: H5
-- Attributes: Total Vacant Housing Units H0050001

\copy (select s.logrecno, sum(h0050001) from sf1_00044 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' group by s.logrecno order by s.logrecno desc) to 'vacantHousingUnits2.csv' with delimiter ',' csv header;



-- NUMBER OF PEOPLE PER HOUSEHOLD
-- Universe: Occupied Housing Units
-- Table: H12
-- Attribute: Average HH Size H0120001

\copy (select s.logrecno, avg(h0120001) from sf1_00044 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' group by s.logrecno order by s.logrecno desc) to 'avgHHSize2.csv' with delimiter ',' csv header;



-- AGE OF MALES
-- Universe: Total Population
-- Table: P12
-- Attribute: Male
--		Under 5 years,P0120003
-- 		5-9 years,P0120004
--		10-14 years,P0120005
--		15 to 17 years,P0120006
--		18 and 19 years,P0120007
--		20 years,P0120008
--		21 years,P0120009
--		22 to 24 years,P0120010
--		25 to 29 years,P0120011
--		30 to 34 years,P0120012
--		35 to 39 years,P0120013
--		40 to 44 years,P0120014
--		45 to 49 years,P0120015
--		50 to 54 years,P0120016
--		55 to 59 years,P0120017
--		60 and 61 years,P0120018
--		62 to 64 years,P0120019
--		65 and 66 years,P0120020
--		67 to 69 years,P0120021
--		70 to 74 years,P0120022
--		75 to 79 years,P0120023
--		80 to 84 years,P0120024
--		85 years and over,P0120025

\copy (select s.logrecno, sum(p0120003), sum(p0120004), sum(p0120005), sum(p0120006), sum(p0120007), sum(p0120008), sum(p0120009), sum(p0120010), sum(p0120011), sum(p0120012), sum(p0120013), sum(p0120014), sum(p0120015), sum(p0120016), sum(p0120017), sum(p0120018), sum(p0120019), sum(p0120020), sum(p0120021), sum(p0120022), sum(p0120023), sum(p0120024), sum(p0120025) from sf1_00004 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' group by s.logrecno order by s.logrecno desc) to 'ageOfMales2.csv' with delimiter ',' csv header;



-- AGE OF FEMALES
-- Universe: Total Population
-- Table: P12
-- Attribute: Female
--		Under 5 years,P0120027
-- 		5-9 years,P0120028
--		10-14 years,P0120029
--		15 to 17 years,P0120030
--		18 and 19 years,P0120031
--		20 years,P0120032
--		21 years,P0120033
--		22 to 24 years,P0120034
--		25 to 29 years,P0120035
--		30 to 34 years,P0120036
--		35 to 39 years,P0120037
--		40 to 44 years,P0120038
--		45 to 49 years,P0120039
--		50 to 54 years,P0120040
--		55 to 59 years,P0120041
--		60 and 61 years,P0120042
--		62 to 64 years,P0120043
--		65 and 66 years,P0120044
--		67 to 69 years,P0120045
--		70 to 74 years,P0120046
--		75 to 79 years,P0120047
--		80 to 84 years,P0120048
--		85 years and over,P0120049

\copy (select s.logrecno, sum(p0120027), sum(p0120028), sum(p0120029), sum(p0120030), sum(p0120031), sum(p0120032), sum(p0120033), sum(p0120034), sum(p0120035), sum(p0120036), sum(p0120037), sum(p0120038), sum(p0120039), sum(p0120040), sum(p0120041), sum(p0120042), sum(p0120043), sum(p0120044), sum(p0120045), sum(p0120046), sum(p0120047), sum(p0120048), sum(p0120049) from sf1_00004 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' group by s.logrecno order by s.logrecno desc) to 'ageOfFemales.csv' with delimiter ',' csv header;


-- TRANSLATE BLOCK NUMBERS TO logrecno

\copy (select block, s.logrecno from sf1_00044 as s, geo_header_sf1 as g where s.logrecno = g.logrecno and g.sumlev = '101' order by block desc) to 'blockToLogrecno.csv' with delimiter ',' csv header;