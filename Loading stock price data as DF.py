 
# Ex1

#import the package "Pandas" into Jupyter Notebook
import pandas as pd

#We import the stock data of Facebook into Jupyter Notebook. The CSV file is located in the folder called "Data" in your Workspace

#Loading Facebook stock data
#We then name the DataFrame name as 'fb'
fb = pd.DataFrame.from_csv('../data/facebook.csv')

#Loading Microsoft stock data
ms = pd.DataFrame.from_csv('../data/microsoft.csv')

# run this cell to ensure Microsoft's stock data is imported
print(ms.iloc[0, 0])
# Result:
46.73

#As seen on: https://hub.coursera-apps.org:443/connect/sharedthedxiky?forceRefresh=false&path=%2Fnotebooks%2Fweek+1%2FImport+data.ipynb

# Ex2

#import the packages "Pandas" and "MatPlotLib" into Jupyter Notebook
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline     ... Note supposed to be commented out...

#import Facebook's stock data
fb = pd.DataFrame.from_csv('../data/facebook.csv')

print(fb.head())
