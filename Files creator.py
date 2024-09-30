import csv

# Define the email body template
Text = """
Here Goes the The Text that You want to create and that will be used so many times so you can double check or ask for the same thing from various people
"""
File=r"Path of.csv" # Put the csv file to help with writing the email or text generation
# Open and read the CSV file
with open(File, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    
    # Loop through each row in the CSV
    for row in reader:
        column1 = row['Column1']
        column2 = row[' column2']  # You can change this to 'Graduate Email' if needed
        # extract the columns that best suits the situation so that you can easily use them later and change their values in the text 
        # Replace the placeholder with the actual university name
        email_body = Text.replace("[column1]", column1) # it is recommanded to put the disred to change column as shown in the Text variable to have  apattren and make error detection more accurate
        
        # Create a .txt file named after the university
        with open(f"{column1}.txt", 'w') as txt_file:
            # Write the email and the email body
            txt_file.write(f"{column2}\n")

print("Files generated successfully!")
