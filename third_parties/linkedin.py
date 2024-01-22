import json
import os

import requests


def scrape_linkedin_profile(linkedin_profile_url: str = "", test_mode: bool = True):
    """Scrape information from a LinkedIn profile,
    Manually scrape the infroamtion from a LinkedIn profile."""

    if test_mode:
        api_endpoint = "https://gist.githubusercontent.com/jorislimonier/2b76951b5431c95c8f1c9a9dcc9a6631/raw/69157b0fcfa883086dbe1b8c3c0084c198e8f7d4/linkedin_joris_limonier.json"
        response = requests.get(api_endpoint)
    else:
        PROXYCURL_API_KEY = os.environ.get("PROXYCURL_API_KEY")
        headers = {"Authorization": "Bearer " + PROXYCURL_API_KEY}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, headers=headers)

    data = response.json()

    # Remove empty fields and fields that are not useful
    removed_fields = ["people_also_viewed", "certifications"]

    data = {
        k: v
        for k, v in data.items()
        if v not in [None, "", []] and k not in removed_fields
    }

    if data.get("groups"):
        for group_dict in data["groups"]:
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    # Pretty print the output
    # print(json.dumps(scrape_linkedin_profile(), indent=4))

    linkedin_data = scrape_linkedin_profile()
    # for k, v in scrape_linkedin_profile().items():
    #     print(f"{k}: {len(str(v))}")

    # Sort keys by length of the value
    for k, v in sorted(linkedin_data.items(), key=lambda item: len(str(item[1]))):
        print(f"{k}: {len(str(v))}")
    print(len(linkedin_data["summary"]))  
    for exp in linkedin_data["experiences"]:
        print(exp)
