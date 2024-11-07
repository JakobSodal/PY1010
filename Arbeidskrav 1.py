# -*- coding: utf-8 -*-
'''
# Arbeidskrav 1 PY1010-1 24H
# Kostnadsbergning samt kostnadsdifferanse av elbil og bensinbil.

av Jakob Sødal (jakobsodal@hotmail.com)

'Oppdatert 04 11 24'

'''
'''
PYTHON-PROGRAM som beregner og presenterer i konsollen de årlige totalkostnadene 
for elbil og for bensinbil samt årlig kostnadsdifferanse ved 10 000 km kjørelengde.

'''

#%% Årlig utgifter i kr: Elbil (10 000 km)

EF = 5000  # Elbilforsikring
T = 8.38*365  # Trafikkforsikringsavgift
ED = 0.2*10000 # Elbil drivstoffbruk 0.2 kWh/km * km kjørt (10 000)
EDK = ED*2      # Elbil drivstoffbruk i kr
EB = 0.1*10000  # Elbil bomavgift 0.1 kr/km * km kjørt (10 000)


print ('Elbil årlig kostnad:', EF + T + EDK + EB,'kr')

#%% Årlige utgifter i kr: Bensinbil (10 000km)

BF = 7500  # Bensinbilforsikring
T  # Trafikkforsikringsavgift (tildelt tidligere)
BD = 1*10000  # Bensinbil drivstoffkostnad 1.0kr/km * km kjørt (10 000k)
BB = 0.3*10000  # Bensinbil bomavgift 0.3 kr/km * km kjørt (10 000)

# Bensinbil årlig kostnad = (BF + T + BD + BB)

print ('Bensinbil årlig kostnad:', BF + T + BD + BB, 'kr')

#%% Kostnadsdifferanse

# Kostnadsdifferanse = (Bensinbil årlig kostnad) - (Elbil årlig kostnad)

print ('Kostnadsdifferanse:', (BF + T + BD + BB) - (EF + T + EDK + EB), 'kr')