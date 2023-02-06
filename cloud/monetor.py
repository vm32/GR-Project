import requests
import pandas as pd
from datetime import datetime

url = input("Enter the URL of the webpage to monitor: ")

response = requests.get(url)

# Convert the response content to a Pandas dataframe
df = pd.read_html(response.content)[0]

# Check the value in the "actions" column
if (df['actions'] > 1).any():
    print("Accident detect")
    print("Time:", df[df['actions'] > 1]['dateandtime'].iloc[0])
