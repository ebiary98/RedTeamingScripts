import shodan
import sys

# Your Shodan API key
API_KEY = "Your_Key"

# Create a Shodan client
api = shodan.Shodan(API_KEY)

# List of search queries to use
queries = [
    "http.title:'Index of /'",
    "port:21",
    "port:22",
    "port:23",
    "port:80",
    "port:443",
    "port:8080",
    "port:3306",
    "http.html:'login'",
    "http.html:'password'",
    "http.html:'username'",
    "http.html:'sign in'",
    "ftp.banner:'220 '",
    "ssh.banner:'SSH-2.0-'",
    "mysql.banner:'5.5.5-'",
    "smb.banner:'Windows '",
    "vnc.product:'VNC'",
    "http.title:'Welcome to the Jenkins'",
    "webmin.title:'Webmin Login'",
    "dns.version:'BIND 9'",
    "snmp.community:'public'",
    "http.html:'Powered by Wordpress'",
    "http.html:'Powered by Joomla'",
    "http.html:'Powered by Drupal'",
    "http.html:'Powered by Magento'",
    "http.html:'Powered by Shopify'",
    "http.html:'Powered by Python'",
    "http.html:'Powered by Ruby'",
]

# Prompt the user for a target (URL or IP address)
target = input("Enter a target (URL or IP address): ")

# Open the output file
with open('shodanRecon.txt', 'w') as f:
    # Iterate over the search queries
    for query in queries:
        try:
            # Use the Shodan API to search for the given query
            results = api.search(query)

            # Print the list of IP addresses and hostnames to the output file
            for result in results['matches']:
                f.write("{} {}\n".format(result['ip_str'], result['hostnames']))
        except Exception as e:
            print("Error: {}".format(e))
            sys.exit(1)
