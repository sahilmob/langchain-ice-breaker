import os
import requests


def scrape_linkedin_profile():
    """scraps a linkedin profile,
    Manually scrape the information for the linkedin profile"""
    api_endpoint = " https://gist.githubusercontent.com/sahilmob/30f8cbff9b3772509608f40c33443b4a/raw/4f59ab4e49e531535b3869ad71766574f14dde23/eden-marco.json"
    response = requests.get(api_endpoint)
    response

    data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications", "inferred_salary"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


# import requests
# api_key = 'NVfz-y_b8dCCULlTJ2sbWg'
# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
# params = {
#     'linkedin_profile_url': 'https://linkedin.com/in/eden-marco/',
#     'extra': 'include',
#     'personal_contact_number': 'include',
#     'personal_email': 'include',
#     'inferred_salary': 'include',
#     'skills': 'include',
#     'use_cache': 'if-present',
#     'fallback_to_cache': 'on-error',
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)
