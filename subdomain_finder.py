import requests
# function created which takes url arg
def request(url):
    # try block serves as a test
    try:
        """try block returns .get() method of request module - 
        it seeks an http addy and truncating https:// infront of it."""
        return request.get("https//" + url)
        """exception works is for if the try blocks fails or runs into an error."""
    except requests.exceptions.ConnectionError:
        # if Connection Error below statement printed
        print("no such subdomain")

target_url = "www.twitter.com"

