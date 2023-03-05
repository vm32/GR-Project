import pandas as pd
tables = pd.read_html("https://vm32.github.io/back.html")
df = tables[0]
print(df.head())
for index, row in df.iterrows():
  if row['Action'] == "Accident":
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
