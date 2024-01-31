from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd
csv_file_path= '2015.csv'

plt.style.use("fivethirtyeight")
   
data=pd.read_csv('2015.csv')
country=data['Country']
hapiness_rank=data['Happiness Rank']

plt.bar(country, hapiness_rank)
plt.title("Happiness Scale")
plt.xlabel('Area')
plt.ylabel("Rank of Happiness")

plt.tight_layout()
plt.savefig('barchartexample.png')
plt.show()