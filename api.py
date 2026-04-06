import requests
import json
import csv
from datetime import datetime

url = "https://api.exchangerate-api.com/v4/latest/USD"

response = requests.get(url)
data = response.json()
timestamp = data["time_last_updated"]
real_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
# 整理部分資料（只取幾個幣別）
result = {
    "base": data["base"],
    "time": real_time,
    "TWD": data["rates"]["TWD"],
    "JPY": data["rates"]["JPY"],
    "EUR": data["rates"]["EUR"],
    "USD": data["rates"]["USD"],
    "CNY": data["rates"]["CNY"],
    "KRW": data["rates"]["KRW"],
    "GBP": data["rates"]["GBP"]
}

# 存 JSON
with open("exchange.json", "w") as f:
    json.dump(result, f, indent=4)

# 存 CSV
with open("exchange.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(result.keys())
    writer.writerow(result.values())

print("匯率資料完成")
