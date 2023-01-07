#!/bin/bash


# Check if a domain was specified as a command-line argument
if [ $# -eq 0 ]; then
  echo "Error: No domain specified." >&2
  exit 1
fi

# Set the domain name that you want to scan
domain=$1

# Check if Amass is installed
if ! [ -x "$(command -v amass)" ]; then
  echo "Error: Amass is not installed." >&2
  exit 1
fi

# Check if Aquatone is installed
if ! [ -x "$(command -v aquatone)" ]; then
  echo "Error: Aquatone is not installed." >&2
  exit 1
fi

# Check if SubFinder is installed
if ! [ -x "$(command -v subfinder)" ]; then
  echo "Error: SubFinder is not installed." >&2
  exit 1
fi

# Check if WaybackURLs is installed
if ! [ -x "$(command -v waybackurls)" ]; then
  echo "Error: WaybackURLs is not installed." >&2
  exit 1
fi

# Use Amass to enumerate subdomains
echo "Running Amass to enumerate subdomains..."
amass enum -d $domain -o amass-output.txt

# Use Aquatone to scan the discovered subdomains and create a report
echo "Running Aquatone to scan subdomains and create a report..."
cat amass-output.txt | aquatone -out aquatone-report

# Use SubFinder to find additional subdomains
echo "Running SubFinder to find additional subdomains..."
subfinder -d $domain -o subfinder-output.txt

# Use WaybackURLs to find historical URLs for the domain
echo "Running WaybackURLs to find historical URLs..."
waybackurls $domain | tee waybackurls-output.txt

echo "Reconnaissance process complete!"
