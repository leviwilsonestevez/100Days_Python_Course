import requests


class DataManager:

    def __init__(self, sheet_price_endpoint: str):
        self.URL = sheet_price_endpoint
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.URL)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {"iataCode": city["iataCode"]}
            }
            sheet_endpoint = f"{self.URL}/{city['id']}"
            response = requests.put(url=sheet_endpoint, json=new_data)
            print(response.text)
