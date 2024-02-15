import csv

# Keywords to exclude from the links
exclude_keywords = ['youtube', 'discord', 'twitch', 'tiktok', 'instagram','facebook', 'twitter', 'streamelements', 'streamlabs','gofundme']

# Read the original CSV and collect all links
with open('extracted_links.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    links = [row['Extracted Link'] for row in reader if row['Extracted Link']]

# Filter links, excluding those containing specified keywords
filtered_links = [link for link in links if all(keyword not in link.lower() for keyword in exclude_keywords)]

# Write the filtered links to a new CSV file
with open('filtered_links.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Filtered Link'])  # Header for the new file
    for link in filtered_links:
        writer.writerow([link])