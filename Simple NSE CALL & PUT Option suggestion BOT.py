# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 24 16:29:26 2020

# @author: Sangram Phadke
# """

# #Simple CALL & PUT suggestion based on NSE Index Direction notifier BOT


# Run time 09:10 , 09:20 : 10:00 , 11:00 , 12:00 , 13:00 , 14:00, 15:00, 15:35

# Output is Text file name "NSEmarket.txt"

################################################# NSE DATA PULL start #################################################

# Importing the libraries
import numpy as np
import pandas as pd
import datetime
from nsetools import Nse
import math
import os
import sys
from pprint import pprint # just for neatness of display
from datetime import datetime
print('############################################################################',file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
pst = datetime.now().strftime("%H:%M")

print('AI Result Start Time',starttime,file=open("NSEmarket.txt", "a"))
print('Disclaimer: All posts are Technology demonstration its not an Financial advice.',file=open("NSEmarket.txt", "a"))
print('Read full Disclaimer at start of the Channel',file=open("NSEmarket.txt", "a"))
print('Overview of Todays Market at time: ',pst,file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
print('Start data pull from NSE server at time ',starttime)
      
print('',file=open("NSEmarket.txt", "a"))

   
# Importing the NIFTY dataset from NSE live site / portel 

nse = Nse()  # NSE object creation

#print (nse)

listallindex = nse.get_index_list()
#lotsize = nse.get_fno_lot_sizes()

#riskmoney = float(input("Enter the Risk/Max Money for trade : "))
riskmoney =5000

# Following variables are use in Option range and risk money caluculations
crkr =0 
prkr = 0
cbrkr = 0
pbrkr = 0
rkr = 0
brkr = 0
bcorm = 0
bporm = 0 
nporm = 0
ncorm = 0

#NIFTY indexs current values

nf_n50 = nse.get_index_quote("nifty 50") 
print('NIFTY 50   index current value is {} and percent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange'])) 


nf_indiavix = nse.get_index_quote("INDIA VIX") 
print('INDIA VIX  index current value is {} and percent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'],'.2f')) 

#nf_200 = nse.get_index_quote("NIFTY 200") 
#print('NIFTY 200  index current value is {} and percent change is {} '.format(nf_200['lastPrice'],nf_200['pChange'],'.2f')) 

nf_bank = nse.get_index_quote("nifty bank") 
print('NIFTY BANK index current value is {} and percent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange'])) 

nf_psubank = nse.get_index_quote("nifty psu bank") 
#print('NIFTY PSU BANK index current value is {} and percent change is {} '.format(nf_psubank['lastPrice'],nf_psubank['pChange'])) 

nf_pvtbank = nse.get_index_quote("nifty pvt bank") 
#print('NIFTY PVT BANK index current value is {} and percent change is {} '.format(nf_pvtbank['lastPrice'],nf_pvtbank['pChange'])) 

nf_finser = nse.get_index_quote("nifty fin service") 
#print('NIFTY Financial service index current value is {} and percent change is {} '.format(nf_finser['lastPrice'],nf_finser['pChange'])) 

nf_auto = nse.get_index_quote("nifty auto") 
#print('NIFTY Auto index current value is {} and percent change is {} '.format(nf_auto['lastPrice'],nf_auto['pChange'])) 

nf_pharma = nse.get_index_quote("nifty pharma") 
#print('NIFTY Pharma index current value is {} and percent change is {} '.format(nf_pharma['lastPrice'],nf_pharma['pChange'])) 

nf_nint = nse.get_index_quote("nifty it") 
#print('NIFTY IT   index current value is {} and percent change is {} '.format(nf_nint['lastPrice'],nf_nint['pChange'])) 

nf_fmcg = nse.get_index_quote("nifty fmcg") 
#print('NIFTY fmcg   index current value is {} and percent change is {} '.format(nf_fmcg['lastPrice'],nf_fmcg['pChange'])) 

nf_energy = nse.get_index_quote("nifty energy") 
#print('NIFTY Energy   index current value is {} and percent change is {} '.format(nf_energy['lastPrice'],nf_energy['pChange'])) 

nf_metal= nse.get_index_quote("nifty metal") 
#print('NIFTY metal index current value is {} and percent change is {} '.format(nf_metal['lastPrice'],nf_metal['pChange'])) 

nf_infra= nse.get_index_quote("nifty infra") 
#print('NIFTY Infra index current value is {} and percent change is {} '.format(nf_infra['lastPrice'],nf_infra['pChange'])) 

nf_consum = nse.get_index_quote("NIFTY CONSUMPTION")
#print('NIFTY CONSUMPTION index current value is {} and percent change is {} '.format(nf_consum['lastPrice'],nf_consum['pChange'])) 

nf_cpse = nse.get_index_quote("nifty CPSE")
#print('NIFTY CPSE index current value is {} and percent change is {} '.format(nf_cpse['lastPrice'],nf_cpse['pChange'])) 

nf_commoditi = nse.get_index_quote("NIFTY COMMODITIES")
#print('NIFTY COMMODITIES index current value is {} and percent change is {} '.format(nf_commoditi['lastPrice'],nf_commoditi['pChange'])) 

nf_servsec = nse.get_index_quote("NIFTY SERV SECTOR")
#print('NIFTY SERVICE SECTOR index current value is {} and percent change is {} '.format(nf_servsec['lastPrice'],nf_servsec['pChange'])) 

nf_media = nse.get_index_quote("NIFTY MEDIA")
#print('NIFTY media SECTOR index current value is {} and percent change is {} '.format(nf_media['lastPrice'],nf_media['pChange'])) 

nf_midcap = nse.get_index_quote("NIFTY MIDCAP 100")
#print('NIFTY Midcap 100 index current value is {} and percent change is {} '.format(nf_midcap['lastPrice'],nf_midcap['pChange'])) 


#Creating data frame for NSE index stocks

dr_nis = pd.read_csv('NSEallsymbol.csv',index_col = 'Symbol')
df_nis = pd.DataFrame(data=dr_nis)


##################      N50   ###########################

df_n50 = df_nis[0:50]

##Retrive NSE live data for each stock as above data frame

nis = []
for i,r in df_n50.iterrows():
    nisl = nse.get_quote(i)
    nis.append(nisl) 

# To make simple list from dictionarys used in above    
nislist=[]

for index in range(len(nis)):
    for key in nis[index]:
        if key == 'symbol':
            #retrive each value
            ins = nis[index]['symbol']
            icn = nis[index]['companyName']
            iop = nis[index]['open']
            iltp = nis[index]['lastPrice']
            ipc = nis[index]['pChange']
            
            #appended values
            nislist.append([ins,icn,iop,iltp,ipc])
    
df_nislist = pd.DataFrame(nislist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_nislist = pd.DataFrame(df_nislist).set_index('symbol')
df_nislist.replace({None: 0.5}, inplace=True)


# N50 shares from NSE

n50grtz = []
n50inzero = []
n50negt = []
for ind in range(len(df_nislist)):
    if (float(df_nislist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        n50grtz.append([itgo,df_nislist.index[ind],df_nislist.iloc[ind][3]])
        
    if (float(df_nislist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        n50negt.append([itlz,df_nislist.index[ind],df_nislist.iloc[ind][3]])
        
    if ((float(df_nislist.iloc[ind][3]) <= 0.99) and (float(df_nislist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        n50inzero.append([itgz,df_nislist.index[ind],df_nislist.iloc[ind][3]])

print("NIFTY 50 stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(n50grtz),len(n50negt),len(n50inzero)))


########################## NBANK ##########################################

df_bank = df_nis[65:104]

##Retrive NSE live data for each stock as above data frame

bank = []
for i,r in df_bank.iterrows():
    bankl = nse.get_quote(i)
    bank.append(bankl) 

# To make simple list from dictionarys used in above    
banklist=[]

for index in range(len(bank)):
    for key in bank[index]:
        if key == 'symbol':
            #retrive each value
            bankns = bank[index]['symbol']
            bankcn = bank[index]['companyName']
            bankop = bank[index]['open']
            bankltp = bank[index]['lastPrice']
            bankpc = bank[index]['pChange']
            #appended values
            banklist.append([bankns,bankcn,bankop,bankltp,bankpc])
    
df_banklist = pd.DataFrame(banklist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_banklist = pd.DataFrame(df_banklist).set_index('symbol')
df_banklist.replace({None: 0.5}, inplace=True)


# Nbank shares from NSE

bankgrtz = []
bankinzero = []
banknegt = []
for ind in range(len(df_banklist)):
    if (float(df_banklist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        bankgrtz.append([itgo,df_banklist.index[ind],df_banklist.iloc[ind][3]])
        
    if (float(df_banklist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        banknegt.append([itlz,df_banklist.index[ind],df_banklist.iloc[ind][3]])
        
    if ((float(df_banklist.iloc[ind][3]) <= 0.99) and (float(df_banklist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        bankinzero.append([itgz,df_banklist.index[ind],df_banklist.iloc[ind][3]])

print("NSE Bank stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(bankgrtz),len(banknegt),len(bankinzero)))



########################## NAUTO #################################

df_auto = df_nis[50:65]

##Retrive NSE live data for each stock as above data frame

auto = []
for i,r in df_auto.iterrows():
    autol = nse.get_quote(i)
    auto.append(autol) 

# To make simple list from dictionarys used in above    
autolist=[]

for index in range(len(auto)):
    for key in auto[index]:
        if key == 'symbol':
            #retrive each value
            autons = auto[index]['symbol']
            autocn = auto[index]['companyName']
            autoop = auto[index]['open']
            autoltp = auto[index]['lastPrice']
            autopc = auto[index]['pChange']
            
            #appended values
            autolist.append([autons,autocn,autoop,autoltp,autopc])
    
df_autolist = pd.DataFrame(autolist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_autolist = pd.DataFrame(df_autolist).set_index('symbol')
df_autolist.replace({None: 0.5}, inplace=True)

# NAUTO shares from NSE

autogrtz = []
autoinzero = []
autonegt = []
for ind in range(len(df_autolist)):
    if (float(df_autolist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        autogrtz.append([itgo,df_autolist.index[ind],df_autolist.iloc[ind][3]])
        
    if (float(df_autolist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        autonegt.append([itlz,df_autolist.index[ind],df_autolist.iloc[ind][3]])
        
    if ((float(df_autolist.iloc[ind][3]) <= 0.99) and (float(df_autolist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        autoinzero.append([itgz,df_autolist.index[ind],df_autolist.iloc[ind][3]])

#print("NSE AUTO stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(autogrtz),len(autonegt),len(autoinzero)))


#############################  NCement ########################################
df_cement = df_nis[104:110]

##Retrive NSE live data for each stock as above data frame

cement = []
for i,r in df_cement.iterrows():
    cementl = nse.get_quote(i)
    cement.append(cementl) 

# To make simple list from dictionarys used in above    
cementlist=[]

for index in range(len(cement)):
    for key in cement[index]:
        if key == 'symbol':
            #retrive each value
            cementns = cement[index]['symbol']
            cementcn = cement[index]['companyName']
            cementop = cement[index]['open']
            cementltp = cement[index]['lastPrice']
            cementpc = cement[index]['pChange']
            #appended values
            cementlist.append([cementns,cementcn,cementop,cementltp,cementpc])
    
df_cementlist = pd.DataFrame(cementlist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_cementlist = pd.DataFrame(df_cementlist).set_index('symbol')
df_cementlist.replace({None: 0.5}, inplace=True)

# Ncement shares from NSE

cementgrtz = []
cementinzero = []
cementnegt = []
for ind in range(len(df_cementlist)):
    if (float(df_cementlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        cementgrtz.append([itgo,df_cementlist.index[ind],df_cementlist.iloc[ind][3]])
        
    if (float(df_cementlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        cementnegt.append([itlz,df_cementlist.index[ind],df_cementlist.iloc[ind][3]])
        
    if ((float(df_cementlist.iloc[ind][3]) <= 0.99) and (float(df_cementlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        cementinzero.append([itgz,df_cementlist.index[ind],df_cementlist.iloc[ind][3]])

#print("NSE cement stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(cementgrtz),len(cementnegt),len(cementinzero)))


############################  NIT  ##################################

df_nint = df_nis[110:121]

##Retrive NSE live data for each stock as above data frame

nint = []
for i,r in df_nint.iterrows():
    nintl = nse.get_quote(i)
    nint.append(nintl) 

# To make simple list from dictionarys used in above    
nintlist=[]

for index in range(len(nint)):
    for key in nint[index]:
        if key == 'symbol':
            #retrive each value
            nintns = nint[index]['symbol']
            nintcn = nint[index]['companyName']
            nintop = nint[index]['open']
            nintltp = nint[index]['lastPrice']
            nintpc = nint[index]['pChange']
            #appended values
            nintlist.append([nintns,nintcn,nintop,nintltp,nintpc])
    
df_nintlist = pd.DataFrame(nintlist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_nintlist = pd.DataFrame(df_nintlist).set_index('symbol')
df_nintlist.replace({None: 0.5}, inplace=True)

# Nnint shares from NSE

nintgrtz = []
nintinzero = []
nintnegt = []
for ind in range(len(df_nintlist)):
    if (float(df_nintlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        nintgrtz.append([itgo,df_nintlist.index[ind],df_nintlist.iloc[ind][3]])
        
    if (float(df_nintlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        nintnegt.append([itlz,df_nintlist.index[ind],df_nintlist.iloc[ind][3]])
        
    if ((float(df_nintlist.iloc[ind][3]) <= 0.99) and (float(df_nintlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        nintinzero.append([itgz,df_nintlist.index[ind],df_nintlist.iloc[ind][3]])

#print("NSE IT stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(nintgrtz),len(nintnegt),len(nintinzero)))

############################  NPOWER  #########################################

df_power = df_nis[121:133]

##Retrive NSE live data for each stock as above data frame

power = []
for i,r in df_power.iterrows():
    powerl = nse.get_quote(i)
    power.append(powerl) 

# To make simple list from dictionarys used in above    
powerlist=[]

for index in range(len(power)):
    for key in power[index]:
        if key == 'symbol':
            #retrive each value
            powerns = power[index]['symbol']
            powercn = power[index]['companyName']
            powerop = power[index]['open']
            powerltp = power[index]['lastPrice']
            powerpc = power[index]['pChange']
            #appended values
            powerlist.append([powerns,powercn,powerop,powerltp,powerpc])
    
df_powerlist = pd.DataFrame(powerlist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_powerlist = pd.DataFrame(df_powerlist).set_index('symbol')
df_powerlist.replace({None: 0.5}, inplace=True)

# Npower shares from NSE

powergrtz = []
powerinzero = []
powernegt = []
for ind in range(len(df_powerlist)):
    if (float(df_powerlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        powergrtz.append([itgo,df_powerlist.index[ind],df_powerlist.iloc[ind][3]])
        
    if (float(df_powerlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        powernegt.append([itlz,df_powerlist.index[ind],df_powerlist.iloc[ind][3]])
        
    if ((float(df_powerlist.iloc[ind][3]) <= 0.99) and (float(df_powerlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        powerinzero.append([itgz,df_powerlist.index[ind],df_powerlist.iloc[ind][3]])

#print("NSE Power stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(powergrtz),len(powernegt),len(powerinzero)))


#############################  Npharma ###########################################

df_pharma = df_nis[133:143]

##Retrive NSE live data for each stock as above data frame

pharma = []
for i,r in df_pharma.iterrows():
    pharmal = nse.get_quote(i)
    pharma.append(pharmal) 

# To make simple list from dictionarys used in above    
pharmalist=[]

for index in range(len(pharma)):
    for key in pharma[index]:
        if key == 'symbol':
            #retrive each value
            pharmans = pharma[index]['symbol']
            pharmacn = pharma[index]['companyName']
            pharmaop = pharma[index]['open']
            pharmaltp = pharma[index]['lastPrice']
            pharmapc = pharma[index]['pChange']
            #appended values
            pharmalist.append([pharmans,pharmacn,pharmaop,pharmaltp,pharmapc])
    
df_pharmalist = pd.DataFrame(pharmalist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_pharmalist = pd.DataFrame(df_pharmalist).set_index('symbol')
df_pharmalist.replace({None: 0.5}, inplace=True)

# Npharma shares from NSE

pharmagrtz = []
pharmainzero = []
pharmanegt = []
for ind in range(len(df_pharmalist)):
    if (float(df_pharmalist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        pharmagrtz.append([itgo,df_pharmalist.index[ind],df_pharmalist.iloc[ind][3]])
        
    if (float(df_pharmalist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        pharmanegt.append([itlz,df_pharmalist.index[ind],df_pharmalist.iloc[ind][3]])
        
    if ((float(df_pharmalist.iloc[ind][3]) <= 0.99) and (float(df_pharmalist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        pharmainzero.append([itgz,df_pharmalist.index[ind],df_pharmalist.iloc[ind][3]])

#print("NSE Pharma stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(pharmagrtz),len(pharmanegt),len(pharmainzero)))



#######################  Niorn ####################################

df_niorn = df_nis[143:161]

##Retrive NSE live data for each stock as above data frame

niorn = []
for i,r in df_niorn.iterrows():
    niornl = nse.get_quote(i)
    niorn.append(niornl) 

# To make simple list from dictionarys used in above    
niornlist=[]

for index in range(len(niorn)):
    for key in niorn[index]:
        if key == 'symbol':
            #retrive each value
            niornns = niorn[index]['symbol']
            niorncn = niorn[index]['companyName']
            niornop = niorn[index]['open']
            niornltp = niorn[index]['lastPrice']
            niornpc = niorn[index]['pChange']
            #appended values
            niornlist.append([niornns,niorncn,niornop,niornltp,niornpc])
    
df_niornlist = pd.DataFrame(niornlist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_niornlist = pd.DataFrame(df_niornlist).set_index('symbol')
df_niornlist.replace({None: 0.5}, inplace=True)

# Nniorn shares from NSE

niorngrtz = []
niorninzero = []
niornnegt = []
for ind in range(len(df_niornlist)):
    if (float(df_niornlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        niorngrtz.append([itgo,df_niornlist.index[ind],df_niornlist.iloc[ind][3]])
        
    if (float(df_niornlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        niornnegt.append([itlz,df_niornlist.index[ind],df_niornlist.iloc[ind][3]])
        
    if ((float(df_niornlist.iloc[ind][3]) <= 0.99) and (float(df_niornlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        niorninzero.append([itgz,df_niornlist.index[ind],df_niornlist.iloc[ind][3]])

#print("NSE Iorn stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(niorngrtz),len(niornnegt),len(niorninzero)))

#############################  NFMCG ###########################################

df_fmcg = df_nis[161:176]

##Retrive NSE live data for each stock as above data frame

fmcg = []
for i,r in df_fmcg.iterrows():
    fmcgl = nse.get_quote(i)
    fmcg.append(fmcgl) 

# To make simple list from dictionarys used in above    
fmcglist=[]

for index in range(len(fmcg)):
    for key in fmcg[index]:
        if key == 'symbol':
            #retrive each value
            fmcgns = fmcg[index]['symbol']
            fmcgcn = fmcg[index]['companyName']
            fmcgop = fmcg[index]['open']
            fmcgltp = fmcg[index]['lastPrice']
            fmcgpc = fmcg[index]['pChange']
            #appended values
            fmcglist.append([fmcgns,fmcgcn,fmcgop,fmcgltp,fmcgpc])
    
df_fmcglist = pd.DataFrame(fmcglist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_fmcglist = pd.DataFrame(df_fmcglist).set_index('symbol')
df_fmcglist.replace({None: 0.5}, inplace=True)

# Nfmcg shares from NSE

fmcggrtz = []
fmcginzero = []
fmcgnegt = []
for ind in range(len(df_fmcglist)):
    if (float(df_fmcglist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        fmcggrtz.append([itgo,df_fmcglist.index[ind],df_fmcglist.iloc[ind][3]])
        
    if (float(df_fmcglist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        fmcgnegt.append([itlz,df_fmcglist.index[ind],df_fmcglist.iloc[ind][3]])
        
    if ((float(df_fmcglist.iloc[ind][3]) <= 0.99) and (float(df_fmcglist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        fmcginzero.append([itgz,df_fmcglist.index[ind],df_fmcglist.iloc[ind][3]])

#print("NSE FMCG stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(fmcggrtz),len(fmcgnegt),len(fmcginzero)))






#############################  Nconstruction  ##########################################

df_cost = df_nis[176:188]

##Retrive NSE live data for each stock as above data frame

cost = []
for i,r in df_cost.iterrows():
    costl = nse.get_quote(i)
    cost.append(costl) 

# To make simple list from dictionarys used in above    
costlist=[]

for index in range(len(cost)):
    for key in cost[index]:
        if key == 'symbol':
            #retrive each value
            costns = cost[index]['symbol']
            costcn = cost[index]['companyName']
            costop = cost[index]['open']
            costltp = cost[index]['lastPrice']
            costpc = cost[index]['pChange']
            #appended values
            costlist.append([costns,costcn,costop,costltp,costpc])
    
df_costlist = pd.DataFrame(costlist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
df_costlist = pd.DataFrame(df_costlist).set_index('symbol')
df_costlist.replace({None: 0.5}, inplace=True)

# Ncost shares from NSE

costgrtz = []
costinzero = []
costnegt = []
for ind in range(len(df_costlist)):
    if (float(df_costlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        costgrtz.append([itgo,df_costlist.index[ind],df_costlist.iloc[ind][3]])
        
    if (float(df_costlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        costnegt.append([itlz,df_costlist.index[ind],df_costlist.iloc[ind][3]])
        
    if ((float(df_costlist.iloc[ind][3]) <= 0.99) and (float(df_costlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        costinzero.append([itgz,df_costlist.index[ind],df_costlist.iloc[ind][3]])

#print("NSE cost stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(costgrtz),len(costnegt),len(costinzero)))


######### Advances Declines
##It containes the number of rising stocks, falling stocks and unchanged stocks in a given trading day, per index.

adv_dec = nse.get_advances_declines()

#pprint(adv_dec)




#####################################  End of dat pull from NSE  ###############################

## End of data pull from NSE
        
endtime = datetime.now().strftime("%H:%M") #program data pull end time
bot_endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print('End of data pull from NSE at time ',endtime)




################################ Print statments #################################################
#Sectors
# print('')
# print("NIFTY 50    stocks where {} are greater than one {} are negative {} are in zeros".format(len(n50grtz),len(n50negt),len(n50inzero)))
# print("NSE AUTO    stocks where {} are greater than one {} are negative {} are in zeros".format(len(autogrtz),len(autonegt),len(autoinzero)))
# print("NSE Bank    stocks where {} are greater than one {} are negative {} are in zeros".format(len(bankgrtz),len(banknegt),len(bankinzero)))
# print("NSE cement  stocks where {} are greater than one {} are negative {} are in zeros".format(len(cementgrtz),len(cementnegt),len(cementinzero)))
# print("NSE IT      stocks where {} are greater than one {} are negative {} are in zeros".format(len(nintgrtz),len(nintnegt),len(nintinzero)))
# print("NSE Power   stocks where {} are greater than one {} are negative {} are in zeros".format(len(powergrtz),len(powernegt),len(powerinzero)))
# print("NSE Pharma  stocks where {} are greater than one {} are negative {} are in zeros".format(len(pharmagrtz),len(pharmanegt),len(pharmainzero)))
# print("NSE Iorn    stocks where {} are greater than one {} are negative {} are in zeros".format(len(niorngrtz),len(niornnegt),len(niorninzero)))
# print("NSE FMCG    stocks where {} are greater than one {} are negative {} are in zeros".format(len(fmcggrtz),len(fmcgnegt),len(fmcginzero)))
# print("NSE Costconstruction stk {} are greater than one {} are negative {} are in zeros".format(len(costgrtz),len(costnegt),len(costinzero)))
# print('')


######################################  Main Logic ##########################################


###### Advances Declines
##It containes the number of rising stocks, falling stocks and unchanged stocks in a given trading day, per index.

#adv_dec = nse.get_advances_declines()

#pprint(adv_dec)

# To make simple list from dictionarys used in above    

adv_dec_list=[]

for index in range(len(adv_dec)):
    for key in adv_dec[index]:
        if key == 'indice':
            #retrive each value
            adv_decid = adv_dec[index]['indice']
            adv_decad = adv_dec[index]['advances']
            adv_decdc = adv_dec[index]['declines']
            adv_decun = adv_dec[index]['unchanged']
            #appended values
            adv_dec_list.append([adv_decid,adv_decad,adv_decdc,adv_decun])
            
    
df_adv_declist = pd.DataFrame(adv_dec_list,columns=['Index Name','Advances','Declines','Unchanged'])        
df_adv_declist = pd.DataFrame(df_adv_declist).set_index('Index Name')
df_adv_declist.replace({None: 0.5}, inplace=True)


adv_dec30 = []
print('Advances Declines calculated for All NIFTY INDEX from NIFTY 50 to NIFT 200: ',file=open("NSEmarket.txt", "a"))

for ind in range(len(df_adv_declist)):
    if (float(df_adv_declist.iloc[ind][1])>= ((df_adv_declist.iloc[ind][0]+df_adv_declist.iloc[ind][2]))):
        itgo = "Declines are more than advances and unchanged in index"
        adv_dec30.append([df_adv_declist.index[ind],df_adv_declist.iloc[ind][1]])
        
if len(adv_dec30) >= len(df_adv_declist)*0.50:
    print('All NIFTY INDEXs Declines are {} at time {}'.format(len(adv_dec30),endtime),file=open("NSEmarket.txt", "a"))
elif (len(adv_dec30) >= len(df_adv_declist)*0.30) and (len(adv_dec30) < len(df_adv_declist)*0.50):
    print('All NIFTY INDEXs Declines are {} at time {}'.format(len(adv_dec30),endtime),file=open("NSEmarket.txt", "a"))
else:
    print('Advance and Decline are {} and Positive at time {} '.format(len(adv_dec30),endtime),file=open("NSEmarket.txt", "a"))
    
print('',file=open("NSEmarket.txt", "a"))
#################################### sectors percentage #####################################

# Sectors	Count	% in N50   innumber
# NAUTO	    15	     0.12	   1.8   2
# NBANK	    38	     0.2	   7.6   8
# NCement	6	     0.04	   0.24  1
# Nconstruction	12	 0.1	   1.2   1
# NFMCG	    15	     0.08	   1.2   1
# Niorn	    18	     0.12	   2.16  2
# NIT	    11	     0.12      1.32  2
# Npharma	10	     0.08      0.8   1
# Npower	12	     0.14	   1.68  2
   
if ((len(autonegt) < 2 and len(banknegt) < 8 and len(cementnegt) < 1 and len(costnegt) < 1 and len(fmcgnegt) < 2 and len(niornnegt) < 2 and len(nintnegt) < 2 and len(pharmanegt) < 1 and len(powernegt) < 2)):
    print('The sectors are up at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
elif(len(autonegt) > 0 and len(banknegt) > 0 and len(cementnegt) > 0 and len(costnegt) > 0 and len(fmcgnegt) > 0 and len(niornnegt) > 0 and len(nintnegt) > 0 and len(pharmanegt) > 0 and len(powernegt) >0 ):
    allsectorl = format((((len(autonegt) + len(banknegt) + len(cementnegt) + len(costnegt) + len(fmcgnegt) + len(niornnegt) + len(nintnegt) + len(pharmanegt) + len(powernegt))/137)*100),'.2f')
    print('All sectors are Down by avrage {} %'.format(allsectorl),file=open("NSEmarket.txt", "a"))
else:
    print('Read full details follows',file=open("NSEmarket.txt", "a"))


if len(autonegt) > 0 :
    # Auto
    autonegtl= format(((len(autonegt)/15)*100),'.2f')
    print ('Auto sector down by {} %'.format(autonegtl,'.2f'),file=open("NSEmarket.txt", "a"))
else:
    print ('Auto sector is up',file=open("NSEmarket.txt", "a"))


if len(banknegt) > 0 :
    #Bank
    banknegtl = format(((len(banknegt)/38)*100),'.2f')
    print ('Bank sector down by {} %'.format(banknegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('Bank sector is up',file=open("NSEmarket.txt", "a"))


if len(nintnegt) > 0 :
    # IT Sector
    nintnegtl = format(((len(nintnegt)/11)*100),'.2f')
    print ('IT sector down by {} %'.format(nintnegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('IT sector is up',file=open("NSEmarket.txt", "a"))


if len(cementnegt) > 0 :
    # Cement
    cementnegtl = format((len(cementnegt)/6)*100,'.2f')
    print ('Cement sector down by {} %'.format(cementnegtl,',2f'),file=open("NSEmarket.txt", "a"))
else:
    print ('Cement sector is up',file=open("NSEmarket.txt", "a"))


if len(costnegt) > 0 :
    # Construction
    costnegtl = format(((len(costnegt)/12)*100),'.2f')
    print ('Construction sector down by {} %'.format(costnegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('Construction sector is up',file=open("NSEmarket.txt", "a"))


if len(fmcgnegt) > 0 :
    # FMCG
    fmcgnegtl= format(((len(fmcgnegt)/15)*100),'.2f')
    print ('FMCG sector down by {} %'.format(fmcgnegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('FMCG sector is up',file=open("NSEmarket.txt", "a"))


if len(niornnegt) > 0 :
    # Iorn
    niornnegtl = format(((len(niornnegt)/18)*100),'.2f')
    print ('Iorn sector down by {} %'.format(niornnegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('Iorn sector is up',file=open("NSEmarket.txt", "a"))


if len(pharmanegt) > 0 :
    # Pharma 
    pharmanegtl = format(((len(pharmanegt)/10)*100),'.2f')
    print ('Pharma sector down by {} %'.format(pharmanegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('Pharma sector is up',file=open("NSEmarket.txt", "a"))

 

if len(powernegt) > 0:
    # Power
    powernegtl = format(((len(powernegt)/12)*100),'.2f')
    print ('Power sector down by {} %'.format(powernegtl),file=open("NSEmarket.txt", "a"))
else:
    print ('Power sector is up',file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))   

###################### IT sector Options ################################# 

print('Todays options trades at time {} are as follows'.format(endtime),file=open("NSEmarket.txt", "a")) 
print('',file=open("NSEmarket.txt", "a"))  
nint_len = len(nintgrtz)+len(nintnegt)+len(nintinzero)

#nint PUT BUY Logic 
if (float(nf_nint['pChange']) <= 0.01) and (float(nf_nint['pChange']) >= -0.75):
    if len(nintnegt) >= (nint_len*0.7) :
        #print('Total negative are more than 70%')
        print('For IT sector stock BUY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        
    else:
        print('Medium Risk to BUY IT sector stock PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For IT sector stock BUY Call at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    

#nint PUT (if previously Buy) Logic
if float(nf_nint['pChange']) < -0.75:
    if (len(nintnegt) >= (nint_len*0.4)) and (len(nintnegt) <= (nint_len*0.7)) :
        #print('Total negative are more than 70%')
        print('For IT sector stock SELL (if previously Buy) PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to SELL (if previously Buy) IT sector stock PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))     
        print('Medium Risk For IT sector stock CALL',file=open("NSEmarket.txt", "a"))        

    
#nint CALL BUY Logic  ##working correctly 
        
if float(nf_nint['pChange']) >= 0.01 and float(nf_nint['pChange']) < 0.75:
    if len(nintnegt) <= (nint_len*0.3) :
        #print('Total negative are less than 20%')
        print('For IT sector stock BUY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to BUY IT sector stock CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High risk For IT sector stock BUY PUT',file=open("NSEmarket.txt", "a"))

              
#nint CALL SELL Logic

        
if float(nf_nint['pChange']) >= 0.75:
    if len(nintnegt) <= (nint_len*0.4) :
        #print('Total negative are less than 20%',file=open("NSEmarket.txt", "a"))
        print('For IT sector stock SELL (if previously Buy) CALL time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to SELL (if previously Buy) IT sector stock CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For IT sector stock BUY PUT ',file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))    

   
###################### N50 Options #################################

print('The NIFTY 50 weekly per lot Option price calculated on Rs. 5000 margin Money',file=open("NSEmarket.txt", "a"))

print('You can increase or decrease per lot Option price depends on your daily margin Money',file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))

#India volatity index
#print('INDIA VIX  index current value is {} and percent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'])) 

#When the vix is go up probability of market direction is continty of same direction is high
#When the vix is % the probability of market direction is continty of same direction is low

# VIX is the persent NIFTY 50 move in positive or negative  // range of trande

# dr_indiavix = pd.read_csv('INDIA_VIX.csv')
# df_indiavix = pd.DataFrame(data=dr_indiavix)
# indiavixdata = {'Date':01-01-2020,'Close':12,'PrevClose':12,'PChange':110}
# df_indiavix = df_indiavix.append(indiavixdata,ignore_index = True)

print('NIFTY 50 index current value is {} and percent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange']),file=open("NSEmarket.txt", "a")) 
print('',file=open("NSEmarket.txt", "a"))    

# NSE all sector indexs belong to NIFTY 50 with respected persent chages are  

financial_service_ni =(float(nf_psubank['pChange']) + float(nf_pvtbank['pChange'])+float(nf_finser['pChange']))*(34.38/100)
info_tech_ni = float(nf_nint['pChange'])*(14.17/100)
consumer_goods_ni = (float(nf_fmcg['pChange'])+float(nf_consum['pChange']))*(13.46/100)
automobile_ni = float(nf_auto['pChange'])*(5.52/100)
pharma_ni = float(nf_pharma['pChange'])*(3.03/100)
metals_ni = float(nf_metal['pChange'])*(2.58/100)
oil_gas_power_ni = (float(nf_energy['pChange'])+float(nf_cpse['pChange']))*(16.86/100)
constuction_ni = float(nf_infra['pChange'])*(2.66/100)
cement_ni =  float(nf_commoditi['pChange'])*(2.31/100)   
services_telecom_ni = float(nf_servsec['pChange'])*(4.13/100)    
media_ni = float(nf_media['pChange'])*(0.36/100)
fertilisers_ni = float(nf_midcap['pChange'])*(0.54/100)


nseindexs = float(financial_service_ni+info_tech_ni+consumer_goods_ni+automobile_ni+pharma_ni+metals_ni+oil_gas_power_ni+constuction_ni+cement_ni+services_telecom_ni+media_ni+fertilisers_ni)

nseindexs = format(nseindexs,'.2f')

print ('NIFTY 50 index at {} %Change and NIFTY 50 Sector index at {} %Change'.format(nf_n50['pChange'],nseindexs),file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))    


#For next month Aprox NIFTY 50 movment in persent:
vixmpc = (float(nf_indiavix['lastPrice'])/3.465) 
nmp = nf_n50['lastPrice']+vixmpc
nmn = nf_n50['lastPrice']-vixmpc

if float(nf_indiavix['pChange']) < 0.0 :
    ndpr = nf_n50['lastPrice']-(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))
else:
    ndpr = nf_n50['lastPrice']+(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))


if float(nf_indiavix['pChange']) > 0.0 :
    ndnr = nf_n50['lastPrice']-(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))
else:
    ndnr = nf_n50['lastPrice']+(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))

ndpf = format(ndpr,'.2f')
ndnf = format(ndnr,'.2f')
ndp = int(50 * round(float(ndpf)/50))
ndn = int(50 * round(float(ndnf)/50))

print("At this time Aprox NIFTY 50 High is {} and low is {} ".format(ndpf,ndnf),file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))    


### VIX   high > 15.811 < low VIX 
#Low VIX Logic
if float(nf_indiavix['lastPrice']) > (15.811-vixmpc) and float(nf_indiavix['lastPrice']) < 15.811:
    print("The VIX is Low ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))
if float(nf_indiavix['lastPrice']) < (15.811-vixmpc):
    print("The VIX is very Low ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))


#HIGH VIX Logic        
if float(nf_indiavix['lastPrice']) > (15.811+vixmpc):
    print("The VIX is Very high ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))
if float(nf_indiavix['lastPrice']) < (15.811+vixmpc) and float(nf_indiavix['lastPrice']) > 15.811:
    print("The VIX is High ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))

#PCR put call ratio 1.68 to 1.8

#highest Open intrest strike price in put and call when NIFTY 50 reach at the strike price sell...

n50_len = len(n50grtz)+len(n50negt)+len(n50inzero)

rkf = format((riskmoney/75),'.2f')
rkr = int(1 * round(float(rkf)/1))

#n50 PUT BUY Logic 
if float(nf_n50['pChange']) <= 0.01 and float(nf_n50['pChange']) > -0.75:
    nporm = 1 # Risk Money variable
    if len(n50negt) >= (n50_len*0.7) :
        if nporm > 0.0:
            prkr = rkr+(rkr*0.20)
            prkr = format(prkr,'.2f')
            print("For NIFTY 50 Buy PE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],prkr),file=open("NSEmarket.txt", "a"))

        else:
            prkr = rkr-(rkr*0.40)
            prkr = format(prkr,'.2f')
            print("For NIFTY 50 Buy PE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],prkr),file=open("NSEmarket.txt", "a"))
    else:
        #print('Medium Risk to BUY NIFTY 50 PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print("Medium Risk to BUY NIFTY 50 PE for {} ITM at max {} Rs".format(ndn-100,prkr),file=open("NSEmarket.txt", "a"))
        print('High Risk For NIFTY 50 BUY Call',file=open("NSEmarket.txt", "a"))


# 1.5% Stratergy for finding range of ITM & OTM
ntwopr = nf_n50['lastPrice']*0.015
ntwop = int(10 * round(float(ntwopr)/10))

if nporm > 0.0:
    prkr = rkr+(rkr*0.20)
    prkr = format(prkr,'.2f')
else:
    prkr = rkr-(rkr*0.40)
    prkr = format(prkr,'.2f')

print("NIFTY 50 Buy PE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],prkr))
print("NIFTY 50 Buy PE for {} ITM at max {} Rs".format(ndn-ntwop,prkr))
print("NIFTY 50 Buy PE for {} OTM at max {} Rs".format(ndp+ntwop,prkr))
print("")


  
#n50 PUT SELL Logic
if float(nf_n50['pChange']) <= -2 and float(nseindexs) < 0.0:
    if (len(n50negt) >= (n50_len*0.4)) and (len(n50negt) <= (n50_len*0.7)) :
        #print('Total negative are more than 70%')
        n50PEITM = ndp
        n50PEATM = (nf_n50['lastPrice'])
        n50PEOTM = ndn
        print('For (if previously Buy) NIFTY 50 SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(n50PEATM,n50PEITM,n50PEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk  to SELL (if previously Buy) NIFTY 50  PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))     
        print('Medium Risk For NIFTY 50 BUY CALL',file=open("NSEmarket.txt", "a"))
        
#n50 CALL BUY Logic  ##working correctly 

if float(nf_n50['pChange']) >= 0.01 and float(nf_n50['pChange']) < 0.85 and float(nseindexs) > 0.0:
    ncorm = -1 # Risk Money variable
    if float(len(n50negt)) <= (n50_len*0.30) :
        if ncorm < 0.0:
            crkr = rkr+(rkr*0.20)
            crkr = format(crkr,'.2f')
            print("For NIFTY 50 Buy CE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],crkr),file=open("NSEmarket.txt", "a"))

        else:
            crkr = rkr-(rkr*0.40)
            crkr = format(crkr,'.2f')
            print("For NIFTY 50 Buy CE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],crkr),file=open("NSEmarket.txt", "a"))
    else:
        #print('Medium Risk to buy NIFTY 50  CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print("Medium Risk to buy NIFTY 50 CE for {} ITM at max {} Rs".format(ndp+100,crkr),file=open("NSEmarket.txt", "a"))
        print('High risk For NIFTY 50 BUY PUT',file=open("NSEmarket.txt", "a") )

if ncorm < 0.0:
    crkr = rkr+(rkr*0.20)
    crkr = format(crkr,'.2f')
else:
    crkr = rkr-(rkr*0.40)
    crkr = format(crkr,'.2f')
        
print("NIFTY 50 Buy CE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],crkr))
print("NIFTY 50 Buy CE for {} ITM at max {} Rs".format(ndp+ntwop,crkr))
print("NIFTY 50 Buy CE for {} OTM at max {} Rs".format(ndn-ntwop,crkr))
print("")
print('',file=open("NSEmarket.txt", "a"))

#n50 CALL SELL Logic
  
if float(nf_n50['pChange']) >= 1.5:
    if len(n50negt) <= (n50_len*0.4) :
        #print('Total negative are less than 20%')
        n50CEITM = (ndn) 
        n50CEATM = (nf_n50['lastPrice'])
        n50CEOTM = (ndp)
        print('For (if previously Buy) NIFTY 50 SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(n50CEATM,n50CEITM,n50CEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to NIFTY 50 50 CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For NIFTY 50 BUY PUT ',file=open("NSEmarket.txt", "a"))



if float(nf_n50['pChange']) <= 0.01 and float(nf_n50['pChange']) > -0.75:print('Buy Put logic')
elif float(nf_n50['pChange']) <= -2 and float(nseindexs) < 0.0:print('Sell Put logic')
elif float(nf_n50['pChange']) >= 0.01 and float(nf_n50['pChange']) < 0.85 and float(nseindexs) > 0.0: print('Buy Call logic')
elif float(nf_n50['pChange']) >= 1.5:print('Sell Call logic')
else:
    print('Hold your NIFTY 50 CE or PE positions for next market move',file=open("NSEmarket.txt", "a"))
    print('Hold your NIFTY 50 CE or PE positions for next market move')


print('',file=open("NSEmarket.txt", "a"))    
    
######################## NBANK Options ###################################



print('BANKNIFTY index current value is {} and percent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange']),file=open("NSEmarket.txt", "a"))
bank_len = (len(bankgrtz)+len(banknegt)+len(bankinzero))
bnseindexsr = (float(nf_psubank['pChange']) * 0.25 + float(nf_pvtbank['pChange']) * 0.74 + float(nf_finser['pChange'])*0.01)

bnseindexs = format(bnseindexsr,'.2f')


print('',file=open("NSEmarket.txt", "a"))  
print ('BANKNIFTY index at {} %Change and NSE BANK Sector index at {} %Change'.format(nf_bank['pChange'],bnseindexs),file=open("NSEmarket.txt", "a"))

#For future prediction depend on NIFTY PSU Bank & PVT Bank Indexs    

if float(nf_psubank['pChange']) > 0.25 and float(nf_pvtbank['pChange']) > 0.75 and float(nf_finser['pChange']) > 0.0:
    #print('Bank sector are in positive at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if len(banknegt) > (bank_len*0.2):
        print('NSE Bank sector is going down but trend is positive',file=open("NSEmarket.txt", "a"))
    else:
        print('Bank sector are in positive at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
elif float(nf_psubank['pChange']) < 0.25 and float(nf_pvtbank['pChange']) < 0.75 and float(nf_finser['pChange']) < 0.0:
    print('Bank sector are in negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if (len(banknegt) > (bank_len*0.4)) and (len(banknegt) < (bank_len*0.70)):
        print('NSE Bank sector is going down and trend is negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    elif len(banknegt) > (bank_len*0.70):
        print('NSE Bank sector is going down and trend is highly negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Bank sector are in positive and trend is negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
else:
    print('Bank sector is sideways at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))



# For BankNifty Weekly Exp.
nf_bankr = int(50 * round(float(nf_bank['lastPrice']/50)))
brkf = format((riskmoney/20),'.2f')
brkr = int(1 * round(float(brkf)/1))
# 1.5% stratergy to calculate the ITM & OTM value
bnonepr = float(nf_bank['lastPrice'])*0.015
bnonep = int(10 * round(float(bnonepr)/10))

#BANK PUT BUY Logic depend on NIFTY Bank Index
if (float(nf_bank['pChange']) > -1) and (float(nf_bank['pChange']) <= 0.01):
    bporm = 1 # Risk Money variable
    if len(banknegt) >= (bank_len*0.55) :
        if bporm > 0.0:
            pbrkr = brkr+(brkr*0.20)
            pbrkr = format(pbrkr,'.2f')
            print("For BANKNIFTY Week buy  PE for  {} ATM at max {} Rs".format(nf_bankr,pbrkr),file=open("NSEmarket.txt", "a"))
        else:
            pbrkr = brkr-(brkr*0.40)
            pbrkr = format(pbrkr,'.2f')
            print("For BANKNIFTY Week buy  PE for  {} ATM at max {} Rs".format(nf_bankr,pbrkr),file=open("NSEmarket.txt", "a"))
    else:
        #print('Medium Risk to BUY BANKNIFTY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print("Medium Risk to buy BANKNIFTY PE for {} ITM at max {} Rs".format((nf_bankr-250),pbrkr),file=open("NSEmarket.txt", "a"))
        print('High Risk For BANKNIFTY BUY CALL',file=open("NSEmarket.txt", "a"))


if bporm > 0.0:
    pbrkr = brkr+(brkr*0.20)
    pbrkr = format(pbrkr,'.2f')
else:
    pbrkr = brkr-(brkr*0.40)
    pbrkr = format(pbrkr,'.2f')
        
print("BANKNIFTY Week buy  PE for  {} ATM at max {} Rs".format(nf_bankr,pbrkr))
print("BANKNIFTY Week buy  PE for  {} ITM at max {} Rs".format((nf_bankr-bnonep),pbrkr))
print("BANKNIFTY Week buy  PE for  {} OTM at max {} Rs".format((nf_bankr+bnonep),pbrkr))
print("")
       
#Bank PUT SELL Logic depend on NIFTY Bank Index
if float(nf_bank['pChange']) <= -1.0:
    if len(banknegt) >= (bank_len*0.4) :
        #print('Total negative are more than 70%')
        bankPEITM = (nf_bank['lastPrice']+100) 
        bankPEATM = (nf_bank['lastPrice'])
        bankPEOTM = (nf_bank['lastPrice']-100)
        print('For (if previously Buy) BANKNIFTY SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(bankPEATM,bankPEITM,bankPEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk  to SELL (if previously Buy) BANKNIFTY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For BANKNIFTY buy CALL',file=open("NSEmarket.txt", "a"))


#Bank CALL BUY Logic depend on NIFTY Bank Index
        
if (float(nf_bank['pChange']) >= 0.01) and (float(nf_bank['pChange']) < 1):
    bcorm = -1 # Risk Money variable
    if len(banknegt) <= (bank_len*0.3) :
        #print('Total negative are less than 20%')
        if bcorm < 0.0:
            cbrkr = brkr+(brkr*0.20)
            cbrkr = format(cbrkr,'.2f')
            print("For BANKNIFTY Week buy  CE for  {} ATM at max {} Rs".format(nf_bankr,cbrkr),file=open("NSEmarket.txt", "a"))
        else:
            cbrkr = brkr-(brkr*0.40)
            cbrkr = format(cbrkr,'.2f')
            print("For BANKNIFTY Week buy  CE for  {} ATM at max {} Rs".format(nf_bankr,cbrkr),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to Buy BANKNIFTY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk to Buy BANKNIFTY PUT  at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))

if bcorm < 0.0:
    cbrkr = brkr+(brkr*0.20)
    cbrkr = format(cbrkr,'.2f')
else:
    cbrkr = brkr-(brkr*0.40)
    cbrkr = format(cbrkr,'.2f')
print("BANKNIFTY Week buy  CE for  {} ATM at max {} Rs".format(nf_bankr,cbrkr))
print("BANKNIFTY Week buy  CE for  {} ITM at max {} Rs".format((nf_bankr+bnonep),cbrkr))
print("BANKNIFTY Week buy  CE for  {} OTM at max {} Rs".format((nf_bankr-bnonep),cbrkr))
print("")

#Bank CALL SELL Logic depend on NIFTY Bank Index
        
if float(nf_bank['pChange']) >= 1.0:
    if len(banknegt) <= (bank_len*0.5) :
        #print('Total negative are less than 50%')
        bankCEITM = (nf_bank['lastPrice']-50) 
        bankCEATM = (nf_bank['lastPrice'])
        bankCEOTM = (nf_bank['lastPrice']+50)
        print('For (if previously Buy) BANKNIFTY SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(bankCEATM,bankCEITM,bankCEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to SELL (if previously Buy) BANKNIFTY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For BANKNIFTY BUY PUT',file=open("NSEmarket.txt", "a"))


print('',file=open("NSEmarket.txt", "a"))

################################### End of BOT ############################################
print('End Time of BOT',bot_endtime,file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
print('End of BOT Read text file "NSEmarket" for results generated / saved at same folder as prrogram')


