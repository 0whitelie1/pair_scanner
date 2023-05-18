import glob

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def make_graph(hisse_1, hisse_2):
    data_1 = pd.read_csv("./data/yahoo/" + hisse_1 + ".csv", delimiter=',')
    data_1 = data_1.dropna(how='any', axis=0)  # cean NULL data

    data_1['Datetime'] = pd.to_datetime(data_1['Datetime'], errors='coerce')
    data_1.set_index("Datetime", inplace=True)
    data_1.rename(columns={"Adj Close": "Adj_Close_1"}, inplace=True)

    data_2 = pd.read_csv("./data/yahoo_price/" + hisse_2 + ".csv", delimiter=',')
    data_2 = data_2.dropna(how='any', axis=0)  # BAZI data_2LAR NULL onları yoktmek

    data_2['Datetime'] = pd.to_datetime(data_2['Datetime'], errors='coerce')
    data_2.set_index("Datetime", inplace=True)
    data_2.rename(columns={"Adj Close": "Adj_Close_2"}, inplace=True)

    merged_data = pd.concat([data_1,data_2["Adj_Close_2"]], join='inner', axis=1)
    merged_data[hisse_1+"/"+hisse_2] = merged_data["Adj_Close_1"] / merged_data["Adj_Close_2"]

    plt.figure(figsize=(10,6))
    plt.plot(merged_data.index, merged_data[hisse_1+"/"+hisse_2], 'b', linestyle='-', markersize=1)
    # plt.plot(data0['Date'], data0['low_trend'], 'g', linestyle='-', markersize=1)
    plt.xlabel('Date Time')
    plt.title(hisse_1+"/"+hisse_2)
    plt.savefig('./output/'+ hisse_1+"_"+hisse_2 + '.png')




### PAIR OLUSTURMA

hisseler = pd.read_csv("./data/spx500.csv", delimiter='\t')


sektorler = hisseler["Sektor"].unique()

for sektor in sektorler:
    hisse_filtered = hisseler[hisseler['Sektor'] == sektor]["Kod"].to_list()

    for count in range (len(hisse_filtered)-1):

        for x in range (1,len(hisse_filtered)):
            if (count+x) < len(hisse_filtered):
                print("Stock: ",  hisse_filtered[count], "/", hisse_filtered[count+x])
                make_graph(hisse_filtered[count],hisse_filtered[count+x])

   

print("Finished, check output folder")
