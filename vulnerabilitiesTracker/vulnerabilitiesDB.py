import csv
import os

# Prompt user to enter client and vulnerability details
print('Enter client and vulnerability details:')
client_name = input('Client Name: ')
name = input('Vulnerability Name: ')
description = input('Description: ')
category = input('Category: ')
severity = input('Severity (low, medium, high, critical): ')
date_discovered = input('Date discovered (YYYY-MM-DD): ')
date_fixed = input('Date fixed (YYYY-MM-DD, leave blank if not fixed yet): ')
remediation_steps = input('Remediation steps: ')

# Database file
database_file = 'vulnerabilities.csv'

# Add vulnerability
vulnerability = {
    'client_name': client_name,
    'name': name,
    'description': description,
    'category': category,
    'severity': severity,
    'date_discovered': date_discovered,
    'date_fixed': date_fixed,
    'remediation_steps': remediation_steps
}

# Create CSV file if it doesn't exist
header = ['Client Name', 'Name', 'Description', 'Category', 'Severity', 'Date Discovered', 'Date Fixed', 'Remediation Steps']
if not os.path.isfile(database_file):
    with open(database_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

# Add vulnerability to CSV file
with open(database_file, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(vulnerability.values())
print('Vulnerability added successfully.')
