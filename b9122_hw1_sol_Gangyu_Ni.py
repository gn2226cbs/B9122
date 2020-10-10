#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:42:16 2020

@author: gangyuni
"""

# =============================================================================
# Q1
# =============================================================================

def compute_emi(PV, FV, rate = 0.04, N = 20):
    
    return (PV + FV/(1+rate ** N) * rate * (1 + rate) ** N / (1+rate) ** N - 1) 
    
while(1):
    try:
        # prompt user to enter values
       fv = int(input("Please enter an integer for future value (FV)"))
       pv = int(input("Please enter an integer for principle amount (PV)"))

    except:
        print("At least one of entered values is not an integer. Please try again.")
    
    else:
        break

print("Equated Monthly Installment (EMI) is {}".format(compute_emi(PV = pv, FV = fv)))


# =============================================================================
# Q2
# =============================================================================
input_file = open('question2.txt', 'r')

str_list = input_file.readlines()

lower_txt = [txt.lower().split() for txt in str_list]

unpacked = list(set([j for i in lower_txt for j in i]))
unpacked.sort(reverse = True, key = lambda l: len(l))

for txt in unpacked:
    print(txt)

# =============================================================================
# Q3
# =============================================================================
#use the Yahoo finance package to download historical stock price data
import yfinance as yf
import matplotlib.pyplot as plt

msft = yf.Ticker('MSFT')
df = msft.history(period = 'max')
df['change'] = df['High'] - df['Low']

df_recent = df.loc['2020-09-01':'2020-09-25']

#Dot/Scatter Plot
plt.scatter(x = df_recent['change'], y = df_recent['Volume'])
plt.title("Microsoft Change in Price vs. Trading Volume in September 2020")
plt.xlabel("Change in Price")
plt.ylabel("Volume")
plt.tight_layout()

plt.show()

# bar plot
plt.bar(df_recent.index, df_recent['Volume'])
plt.title("Microsoft Daily Volume in September 2020")

plt.tight_layout()
plt.show()


# boxplot
plt.boxplot(df_recent['Volume'])
plt.xticks([1],['Microsoft Volume'])
plt.title("Microsoft Daily Volume in September 2020")
plt.show()

# pie chart

df_mar = df.resample('M').mean().loc['2020-01-01':'2020-06-01']
labels = df_mar.index

plt.pie(df_mar['Volume'], labels = labels, autopct='%1.2f%%')
plt.title("MSFT Average Monthly Trading Volume in COVID-19 Pandamic Selloff")
plt.show()

