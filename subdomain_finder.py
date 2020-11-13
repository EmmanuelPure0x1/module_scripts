import requests


# function created which takes url arg
def request(url):
    # try block serves as a test
    try:
        """try block returns .get() method of request module - 
        it seeks an http addy and truncating https:// infront of it."""
        return requests.get("https://" + url)

        # exception works is for if the try blocks fails or runs into an error.
    except requests.exceptions.ConnectionError:
        # if Connection Error below statement printed
        # print("no such subdomain")
        pass


url = "www.twitter.com"

#------------"""SUBDOMAIN Finder"""---------------#

target_url1 = "twitter.com"

# Opening wordlist location using "with open()", specifying reading mode ('r') and storing value of search as 'file'
with open("C:\\Users\\D--\\PycharmProjects\\modules_scripts\\wordlist\\sub_word_list.txt", 'r') as file:
    # iterating over each line within file
    for line in file:
        # stripping all white spaces that may be included in the line
        word = line.strip()
        # concatenating result of word var, full stop and target url 1 variable
        test_url = word + "." + target_url1
        # storing request
        response = request(test_url)

        if response:
            print(f"Subdomain: {test_url}, exists.")
        else:
            print(f"{test_url} >> no response.")
