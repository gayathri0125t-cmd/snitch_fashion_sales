import pandas as pd
df = pd.read_csv(r"C:\Users\Gayathri\Downloads\Snitch_Fashion_Sales_Uncleaned.csv")
print(df.head())  #read 5 heads
print(df.info())
print(df.describe())
print(df.isnull().sum())  #null values
df = df.dropna()  # null rows
print(df.columns)
df.columns = df.columns.str.upper().str.strip().str.replace(" ", "_") #upper case
df = df.drop_duplicates()  #duplicate record
df.columns = df.columns.str.lower().str.replace(" ", "_")  # convert date
df.to_csv(r"C:\Users\Gayathri\Downloads\Snitch_Fashion_Sales_Cleaned.csv", index=False)
