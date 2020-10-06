import requests # Imports requests library

try:
    response = requests.get("https://catfact.ninja/fact") # Get API
    print(response.status_code) # Displays status code to user
    response.raise_for_status() # Will raise an exception for 400 or 500 status codes

    print(response.text) # Displays API response to user
    print(response.json()) # Displays API response to user

    data = response.json() # Assigns API response to variable "data"
    fact = data["fact"] # Assigns API response to variable "fact"
    print(f"A random cat fact is: {fact}") # Displays API response as user-friendly message

except Exception as e: # Exception handling for error messages to user
    print(e) # Display exception
    print("There was an error making the request.") # Display user-friendly error message
