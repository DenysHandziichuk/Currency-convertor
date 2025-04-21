import requests
import tkinter as tk

window = tk.Tk()
window.geometry("200x200")
window.title("Currency Converter")

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates'][target_currency]

def currency_convertor(amount, exchange_rate):
    return amount * exchange_rate

def convert():
    amount = float(amount_entry.get())
    base_currency_value = base_currency.get()
    target_currency_value = target_currency.get()
    exchange_rate = get_exchange_rate(api_key, base_currency_value, target_currency_value)
    converted_amount = currency_convertor(amount, exchange_rate)
    result_label.config(text=f"{amount} {base_currency_value} is equal to {converted_amount:.2f} {target_currency_value}")

api_key = 'enter api key here'
amount_label = tk.Label(window, text="Enter amount of base currency: ",)
amount_label.pack()
amount_entry = tk.Entry(window, width=10)
amount_entry.pack()

base_currency_label = tk.Label(window, text="Enter base currency: ",)
base_currency_label.pack()
base_currency = tk.Entry(window, width=10)
base_currency.pack()

target_currency_label = tk.Label(window, text="Enter target currency:")
target_currency_label.pack()
target_currency = tk.Entry(window, width=10)
target_currency.pack()

convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

result_label = tk.Label(window)
result_label.pack()

window.mainloop()
