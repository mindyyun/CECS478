"""
Authors: Emma Tu, Mindy Yun
Contribution: Emma 50%, Mindy 50%
"""

import requests
from requests.exceptions import SSLError

# Website to test (you can change this)
url = "https://www.google.com"

try:
    # Send request (SSL verification is ON by default)
    response = requests.get(url)

    # If no error, SSL certificate is valid
    print("SSL Certificate is VALID")
    print("Status Code:", response.status_code)

except SSLError as e:
    # If SSL fails
    print("SSL Certificate is INVALID")
    print("Error:", e)

except Exception as e:
    # Any other error
    print("Other Error:", e)