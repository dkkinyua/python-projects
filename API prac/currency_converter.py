# This is a currency converter programn using API's and JSON using the Frankfurter API

import requests


from_currency = str(
    input("Enter the currency you would like to convert from: ")).upper()
to_currency = str(
    input("Enter the currency you would like to convert to: ")).upper()
amount = float(input("Enter the amount to be converted: "))
response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
return_statement = print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]}{to_currency}")
print(return_statement)
