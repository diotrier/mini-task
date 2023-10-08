import requests
from datetime import datetime
from pprint import pprint

# input API
city = "Jakarta"
API_key = "cc22b1c64e85d37cb9c930887b6051c8"
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},id&appid={API_key}"

# cek API
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    # pprint(data)

    # variable data tanggal
    last_date = ""

    # main section
    print("Ramalan Cuaca Jakarta Untuk 5 hari ke depan")
    for forecast in data["list"]:
        date_time = forecast["dt_txt"]
        date = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S").strftime(
            "%a, %d %b %Y"
        )
        temp = forecast["main"]["temp"] - 273.15  # convert suhu dari kelvin ke celcius

        # print hasil ramalan cuaca di jakarta
        if date != last_date:
            print(f"{date}: {temp:.2f}°C")
            last_date = date
else:
    print("API tidak connect")
