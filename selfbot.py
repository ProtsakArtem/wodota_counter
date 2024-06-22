from datetime import datetime, timedelta
import requests
import time

url = "https://discord.com/api/v9/users/@me/profile"

token = "token"
start_date = datetime(2024, 5, 21)

def change_bio():
    days_count = (datetime.now() - start_date).days
    if days_count %10 == 1:
        text = f"{days_count}/365 день без доти"
    elif days_count %10 == 2 or days_count %10 == 3 or days_count %10 == 4 or days_count:
        text = f"{days_count}/365 дні без доти"
    else:
        text = f"{days_count}/365 днів без доти"
    header = {
        "authorization": token,
    }
    json_data = {
        "bio": text
    }

    requests.patch(url, json=json_data, headers=header)
    print( requests.patch(url, json=json_data, headers=header))
    print(json_data, header, text)


while True:
    change_bio()
    print("ok")
    time.sleep(86400)
