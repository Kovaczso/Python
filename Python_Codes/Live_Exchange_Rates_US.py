## This is a program that using BeautifulSoup to scrape a website.
## Using pandas lirbary creating a dataframe with 51 different currencies converted to USD
## Ultimatelly saving it as a csv. 

## NOTE: Program also uses "Exchange_rates.csv" file that containg Currency names and codes.  

from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.x-rates.com/table/?from=USD&amount=1'

page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'html')

table = soup.find_all('table')[1]


columns = table.find('tr')
headers = columns.find_all('th')
header_columns = [title.text.strip() for title in headers ]


df = pd.DataFrame (columns = header_columns)
df
column_data = table.find_all('tr')


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    
    lenght = len(df)
    df.loc[lenght] = individual_row_data


df.head(5)


from datetime import datetime

current_date = datetime.today().date()
df['Day_DT'] = current_date
df.head(5)
df.drop_duplicates()


csv_file = (r"C:\Users\zsolt\Desktop\Python Files\Exchange_rates.csv")
csv_file = csv_file.replace("\\", "/")
df2 = pd.read_csv(csv_file)[["Currency_Name","Currency_Code"]]

merged_df = df.merge(df2[['Currency_Name','Currency_Code']],
                    left_on='US Dollar',
                    right_on='Currency_Name',
                    how='left')

merged_df = merged_df.drop(columns=['Currency_Name'])

columns_order =['Day_DT','US Dollar','Currency_Code','1.00 USD','inv. 1.00 USD']

merged_df = merged_df[columns_order]

merged_df.head(5)


usd_df = merged_df.rename(columns={'Day_DT':'DAY_DT','US Dollar': 'CURRENCY_NAME','Currency_Code':'CURRENCY','1.00 USD':'TO_USD','inv. 1.00 USD':'FROM_USD'})

usd_df.head(5)


storage = r'C:\Users\zsolt\Desktop\Python Files'
file_name = "US_Rates.csv"
storage = storage.replace("\\", "/")
storage = storage + "/" + file_name
df.to_csv(storage,index = False)

## This program is set to save the file on your local machine
## Although you can use Google Colab to save the file in a GitHub repository and schedule it as frequently as want. 
