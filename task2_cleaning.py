import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
import csv

df=pd.read_csv("Level1/quotes.csv")

#for missing data;
df.fillna("Unknown",inplace=True)

#for duplicates;
df.drop_duplicates(inplace=True)

#Removing Quotation Marks;
df["Quote"] = df["Quote"].str.replace('“', '', regex=False)
df["Quote"] = df["Quote"].str.replace('”', '', regex=False)
df['Quote'] = df['Quote'].str.strip('"')

#for converting categorical variables into numerical format
le=LabelEncoder()
df["Author_Encoded"]=le.fit_transform(df["Author"])
df["Tag_Encoded"]=le.fit_transform(df["Tag"])

#numberical feature for normalization
df["Quote_Length"]=df["Quote"].apply(len)

#standardize numerical data
scaler=StandardScaler()
df["Quote_Length_Scaled"]=scaler.fit_transform(df[["Quote_Length"]])

#saving the data
df.to_csv("cleaned_quotes.csv",index=False,quoting=csv.QUOTE_MINIMAL)
print("Data cleaned and preprocessed successfully")
print(df.head())