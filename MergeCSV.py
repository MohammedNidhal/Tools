import os
import pandas as pd

def merge_csv_files(directory, output_file):
    allDataCSV = []
    
    # Iterate over all files in the directory
    for file in os.listdir(directory):
        if file.endswith('.csv'):
            file_path = os.path.join(directory, file)
            # Read the csv file into a dataframe
            df = pd.read_csv(file_path)
            allDataCSV.append(df)
    
    # Concatenate all dataframes into one
    ResultDf = pd.concat(allDataCSV)
    
    # Remove duplicate rows
    ResultDf.drop_duplicates(inplace=True)

    ResultDf.to_csv(output_file, index=False)
    print(f"Merged CSV saved to {output_file}")


directory_path = 'CSV Directory'  
output_csv = 'NameofMerged.csv'  

merge_csv_files(directory_path, output_csv)
