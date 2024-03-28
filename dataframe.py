
import pandas as pd
import json

# Path to the CSV file
csv_file_path = 'Hyscaler.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Extract base URLs
df['Base_URL'] = df['URL'].str.extract(r'(https://example.com/data/\w+)')

# Group by base URL and aggregate descriptions
grouped = df.groupby('Base_URL')['Description'].apply(list).reset_index()

# Convert DataFrame to list of dictionaries
result = []
for _, row in grouped.iterrows():
    base_url = row['Base_URL']
    descriptions = row['Description']
    url_dict = {'URL': base_url}
    for i, desc in enumerate(descriptions, start=1):
        # Replace or remove the en dash character
        desc = desc.replace('\u2013', '-')  # Replace with a hyphen
        # desc = desc.replace('\u2013', '')  # Remove altogether
        url_dict[f'desc{i}'] = desc
    result.append(url_dict)

# Write the result to a JSON file
output_file_path = 'output.json'
with open(output_file_path, 'w') as json_file:
    json.dump(result, json_file, indent=2)

print('JSON file created successfully:', output_file_path)
