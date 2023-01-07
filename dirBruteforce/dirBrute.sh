#!/bin/bash

# Prompt the user to enter the target URL
read -p "Enter the target URL: " url

# Set the wordlist and output file
wordlist="/usr/share/dirb/wordlists/common.txt"
output_file="dirb-results.txt"

# Check if DirB and DirBuster are installed
if ! [ -x "$(command -v dirb)" ]; then
  echo "Error: DirB is not installed." >&2
  exit 1
fi


# Perform the directory bruteforce attack with DirB
echo "Running directory bruteforce attack with DirB..."
dirb "$url" "$wordlist" >> "$output_file"


echo "Directory bruteforce attacks complete! Results saved to $output_file."
