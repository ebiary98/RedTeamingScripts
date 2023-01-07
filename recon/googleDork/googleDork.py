import requests
import re
import sys

# Set the base URL for the Google search API
base_url = 'https://www.googleapis.com/customsearch/v1'

# Set the API key and search engine ID
api_key = 'Your_API_Key'
search_engine_id = 'Your_Search_Engine_id'
domain1="jsfiddle.net"
domain2="codebeautify.org"
domain3="codepen.io"
domain4="pastebin.com"

# Set the target domain
if len(sys.argv) < 2:
    print('Usage: python dorking.py TARGET_URL')
    sys.exit()
domain = sys.argv[1]

# Set the search queries

queries = [
    "site:" + domain,
    "site:" + domain + " inurl:login",
    "site:" + domain + " intext:password",
    "site:" + domain + " inurl:admin",
    "site:" + domain + " filetype:xlsx",
    "site:" + domain + " filetype:docx",
    "site:" + domain + " filetype:pdf",
    "site:" + domain + " intext:username",
    "site:" + domain + " intext:email",
    "site:" + domain + " intext:phone",
    "site:" + domain + " intext:credit",
    "site:" + domain + " intext:bank",
    "site:" + domain + " intext:social",
    "site:" + domain + " intext:ssn",
    "site:" + domain + " intext:security",
    "site:" + domain + " inurl:signup",
    "site:" + domain + " inurl:register",
    "site:" + domain + " intext:user",
    "site:" + domain + " filetype:sql",
    "site:" + domain + " filetype:csv",
    "site:" + domain + " filetype:txt",
    "site:" + domain + " inurl:backup",
    "site:" + domain + " inurl:dump",
    "site:" + domain1 + " domain",
    "site:" + domain2 + " domain",
    "site:" + domain3 + " domain",
    "site:" + domain4 + " domain",
    "site:" + domain + " inurl:export",
]



# Set the number of results to retrieve
num_results = 10

# Set the user agent string
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# Set the headers
headers = {'User-Agent': user_agent}

# Set the parameters for the search
params = {
    'key': api_key,
    'cx': search_engine_id,
    'num': num_results
}

# Iterate over the search queries
for query in queries:
    # Set the search query
    params['q'] = query

    # Set the starting index for the results
    params['start'] = 1

    # Send the request to the Google search API
    response = requests.get(base_url, params=params, headers=headers)

    # Check the status code of the response
    if response.status_code == 200:
        # Parse the response to get the list of results
        results = response.json()['items']
        

        # Print the results
        for result in results:
            print(result['link'])
    else:
        print('An error occurred:', response.status_code)
