import requests

def get_quote_of_day():
    url = 'https://quotes.rest/qod?languague=en'
    api_token = "They Said so"
    headers = {'content-type': 'application/json',
               'X-TheySaidSo-Api-Secret': format(api_token)}

    response = requests.get(url, headers=headers)
    # print(response)
    quotes = response.json()['contents']['quotes'][0]

    return quotes