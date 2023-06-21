import json
from urllib.request import urlopen

def main():
    print("Please enter currencies in small letter abbreviation. Like, american dollar will be usd")
    print(converter())
    
def converter():
    with urlopen("http://www.floatrates.com/daily/usd.json") as response:
        source = response.read()
        source = source.decode("utf-8")  
        data = json.loads(source)
    
    for curr in data:
        name = data[curr]['name']
        price = data[curr]['rate']
        
    currency = input('Currency you want to convert: ')
    if currency == 'usd':
        curr_name = "USD"
        curr_rate = 1.0
    else:    
        curr_name = data[currency]['name']
        curr_rate = data[currency]['rate']
    
    converted_curr = input('Convert to: ')
        
    if converted_curr == "usd":
        conv_curr_name = "USD"
        converted_curr_rate = 1.0
        
    else:
        conv_curr_name = data[converted_curr]['name']
        converted_curr_rate = data[converted_curr]['rate']
    
    currency_amt = input("Currency amount: ")
    currency_amt = float(currency_amt)
    return f"{currency_amt:.2f} {curr_name} is {currency_amt*(converted_curr_rate/curr_rate):.2f} {conv_curr_name}."

if __name__ == "__main__":
    main()
