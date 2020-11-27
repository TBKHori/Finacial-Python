#import the package "Pandas" into Jupyter Notebook
import pandas as pd

#We import the stock data of Facebook into Jupyter Notebook. The CSV file is located in the folder called "Data" in your Workspace
#We then name the DataFrame name as 'fb'
fb = pd.DataFrame.from_csv('../data/facebook.csv')

ms = pd.DataFrame.from_csv('../data/microsoft.csv')

# run this cell to ensure Microsoft's stock data is imported
print(ms.iloc[0, 0])
# Result:
46.73

#As seen on: https://hub.coursera-apps.org:443/connect/sharedthedxiky?forceRefresh=false&path=%2Fnotebooks%2Fweek+1%2FImport+data.ipynb