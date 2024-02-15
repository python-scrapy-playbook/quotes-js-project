import csv

# Keywords to exclude from the links
exclude_keywords = ['youtube', 'discord', 'twitch', 'patreon']

# Open the existing CSV file for reading
with open('extracted_links.csv', mode='r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Skip header row

    # Open a new CSV file to write the filtered results
    with open('filtered_links.csv', mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the header to the new file

        # Iterate over each row in the original file
        for row in reader:
            # Check if the URL does not contain any of the excluded keywords
            if not any(keyword in url.lower() for keyword in exclude_keywords):
                writer.writerow(row)  # Write the row to the new file if it passes the filter