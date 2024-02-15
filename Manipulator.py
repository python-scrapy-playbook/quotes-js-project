import csv

input_file_path = 'results.csv'  # Adjust to your actual CSV file
output_file_path = 'quotes_5_output_modified.csv'  # Desired output file name

# Open the input CSV file for reading and the output file for writing
with open(input_file_path, 'r', newline='') as infile, open(output_file_path, 'w', newline='') as outfile:
    # Read the file line by line
    for line in infile:
        # Remove unwanted characters
        # Assuming the URL is the only content in each row or is the first column
        clean_line = line.strip().replace('"', '')  # Remove double quotes
        if clean_line:  # Check if line is not empty
            outfile.write(clean_line + "\n")  # Write the cleaned line to the output file
