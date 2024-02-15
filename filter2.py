import csv

# Keywords to exclude from the links
exclude_keywords = ['youtube', 'discord', 'twitch']

# Read the original CSV file
with open('extracted_links.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    filtered_links = []

    # Filter URLs
    for row in reader:
        url = row['Extracted Link']
        if not any(keyword in url.lower() for keyword in exclude_keywords):
            filtered_links.append(row)

# Write the filtered URLs to a new CSV file
with open('filtered_links.csv', mode='w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['URL', 'Extracted Link']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_links)