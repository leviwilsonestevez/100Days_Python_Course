import requests


class DataManager:

    def __init__(self, sheet_price_endpoint: str, sheet_users_endpoint: str):
        self.URL_PRICE_ENDPOINT = sheet_price_endpoint
        self.destination_data = {}
        self.customer_data = {}
        self.URL_USER_ENDPOINT = sheet_users_endpoint

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self.URL_PRICE_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {"iataCode": city["iataCode"]}
            }
            sheet_endpoint = f"{self.URL_PRICE_ENDPOINT}/{city['id']}"
            response = requests.put(url=sheet_endpoint, json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = self.URL_USER_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
