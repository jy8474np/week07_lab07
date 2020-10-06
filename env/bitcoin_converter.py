import requests # Imports requests library 

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") # Get API
    response.raise_for_status() # Raise exception for 400 or 500 codes
    
    data = response.json() # Assigns API response to variable "data"
    usd_exchange_rate = data["bpi"]["USD"]["rate_float"] # Within "data" API response locate the desired information

    usd = float(input("Please enter the value in USD: $")) # Obtain from user USD amount to be converted
    converted = (usd * usd_exchange_rate) # Calculate conversion from USD to Bitcoin
    print(f"${usd} USD is currently equal to {converted} Bitcoin.") # Display results in a user-friendly format

except Exception as e: # Exception handling for error message to user
    print(e) # Display exception
    print("There was an error completing your request.") # Display user-friendly error message 
