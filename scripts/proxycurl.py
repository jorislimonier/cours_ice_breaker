import requests
import os

if __name__ == "__main__":
    print(os.environ.get("PROXYCURL_API_KEY"))

    PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")
    headers = {"Authorization": "Bearer " + PROXYCURL_API_KEY}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    params = {
        "linkedin_profile_url": "https://linkedin.com/in/jorislimonier",
    }
    response = requests.get(api_endpoint, params=params, headers=headers)

    print(response.json())
