import pandas as pd

# Use the read_html method from pandas to extract tables from a website
tables = pd.read_html("https://vm32.github.io/back.html")

# The read_html method returns a list of dataframes, so you can access the desired table by indexing the list
df = tables[0]

# You can now manipulate and analyze the data in the dataframe just like any other pandas dataframe
print(df.head())

# Iterate over each row in the dataframe
for index, row in df.iterrows():
  if row['Action'] == "Accident":
    # Access data for each column by column name
    print("Index: ", index)
    print("GPS_ID: ", row["GPS_ID"])
    print("Plate Number: ", row["Plate Number"])
    print("Latitude: ", row["Lat"])
    print("Longlitude: ", row["Long"])
    print("Date: ", row["Date"])
    print("Time: ", row["Time"])
    print("Action: ", row["Action"])
    print("-----------------------------")

  else:
    pass
