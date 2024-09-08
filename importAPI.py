import requests
import csv
import pandas as pd

url = "https://api.nbp.pl/api/exchangerates/tables/C?format=json"
response = requests.get(url)
data = response.json()

csv_filename = "nbp_exchange_rates.csv" # można zapisać na dysk jako np: r"C:\Kodilla\nbp_exchange_rates.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Currency", "Code", "Bid", "Ask"])
    for item in data[0]["rates"]:
        writer.writerow([item["currency"], item["code"], item["bid"], item["ask"]])

csv_filename
csv_file_path = "nbp_exchange_rates.csv"
df = pd.read_csv(csv_file_path)
print(df.head())