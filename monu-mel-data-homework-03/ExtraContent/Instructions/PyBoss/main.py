# main.py

import os
import csv 

# US abbrivated states
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# Initializing file paths.
csv_read_file_path = "employee_data.csv"
csv_write_file_path = "employee_data_output.csv"

# Setup csv reader.
with open(csv_read_file_path) as csv_read_file:
    csv_reader = csv.DictReader(csv_read_file, delimiter=',')
    
    # Setup csv writer.
    with open(csv_write_file_path, mode='w') as csv_write_file:
        csv_writer = csv.writer(csv_write_file, delimiter=',')

        # Change data of each row and write row to output file
        for row in csv_reader:
            # Reformat dob
            row['DOB'] = f"{row['DOB'][5:7]}/{row['DOB'][-2:]}/{row['DOB'][:4]}"
            # Obscure fist 5 digits of SSN
            row['SSN'] = f"***-**-{row['SSN'][-4:]}"
            # Split name to first and last and put in new columns
            first_name, last_name = row.pop('Name').split(' ')
            row['First Name'] = first_name
            row['Last Name'] = last_name
            # Abbreviate state name
            row['State'] = us_state_abbrev.get(row['State'])
            csv_writer.writerow([row['Emp ID'], row['First Name'], row['Last Name'], row['DOB'], row['SSN'], row['State']])

    