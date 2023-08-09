import os
import requests
from dotenv import load_dotenv
load_dotenv()

def api(longURL):
    key = os.getenv("API_KEY")
    userURL = longURL
    apiURL = f"http://cutt.ly/api/api.php?key={key}&short={userURL}"
    data = requests.get(apiURL).json()["url"]
    if data["status"] == 7:
        return data["shortLink"]
    else:
        error = data["status"]
        print(f"Error code: {error}")
        exit()

def main():
    url = input("Enter URL to shorten: ")
    shortened = api(url)
    try:
        print(f"Shortened URL: {shortened}")
    except:
        print("An error has occured")

if __name__ == "__main__":
    main()