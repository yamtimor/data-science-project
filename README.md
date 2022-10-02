#Data Science Project Protocol
Introduction
We decided to start with simple predictive model- take criminal records in Israel (origin: https://data.gov.il/dataset/crime_records_data
we use the first file -  פירוט של תיקי פשיעה לפי אזור רבעון וסוגי עבירות)

The questions do we want to answer: Predicting felons over time - region - type (By clustering?)

#need to do:

#About the data: 643493 observations include:
ArealAttributionType סיווג של השיוך הגאוגרפי של התיקים - X
PoliceDistrict המחוז שבתחומו התרחשו העבירות - V
PoliceMerhav המרחב שבתחומו התרחשו העבירות - V
PoliceStation התחנה שבתחומה התרחשו העבירות- V
Settlement_Council הישוב, או המועצה האזורית, או המקום שבתחומם התרחשו העבירות- X
StatArea  האזור הסטטיסטי שבתחומו התרחשו העבירות - DROP THIS VARIABLE
Quarter רבעון ושנה בהם קרו העבירות- V
StatisticCrimeGroup קבוצת העבירה- V
StatisticCrimeType סיווג העבירה- V
TikimSum כמות תיקי הפשיעה- V

#Documentation of cleansing the data:
- Change values of 'StatisticCrimeGroup','StatisticCrimeType' in order not to have duplicates values
- 


You can try to answer to the following question:
Which 
?
What is known about the problem?
How do we define the outcome(s)?
What is known to influence the outcome?
Does we have any possible new knowledge that has not been in use before?
This part must be between half to one and half page.

