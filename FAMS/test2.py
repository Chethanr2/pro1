import pandas as pd


df = pd.read_excel('C:/Users/Chethan/Desktop/Stops_Input.xlsx')
lat = df['B'][8]
print(lat)