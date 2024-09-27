import pandas as pd
import webbrowser
import urllib.parse

# Function to perform a Google search for each term
def google_search(search_query):
    query = urllib.parse.quote_plus(search_query)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Read the CSV file
def search_from_csv(csv_file, column_name):
    # Load the CSV into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Ensure the column exists
    if column_name in df.columns:
        # Loop through the column and perform Google searches
        for item in df[column_name]:
            google_search(str(item))
    else:
        print(f"Column '{column_name}' not found in the CSV file.")

# Specify the CSV file and column name
csv_file = r"PATH TO CSV FILE"  # Replace with your CSV file path
column_name = 'COLUMN_NAME'  # Replace with the column name you want to search

# Run the search function
search_from_csv(csv_file, column_name)
