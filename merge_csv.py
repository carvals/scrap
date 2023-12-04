import pandas as pd
import glob

def merge_csv_files(folder_path, output_file='merged.csv'):
    # Find all CSV files in the specified folder
    csv_files = glob.glob(f'{folder_path}/*.csv')

    # Check if there are any CSV files
    if not csv_files:
        print(f"No CSV files found in the folder: {folder_path}")
        return

    # Create an empty DataFrame to store the merged results
    df_merged = pd.DataFrame()

    # Read and concatenate each CSV file
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df_merged = pd.concat([df_merged, df], ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    df_merged.to_csv(output_file, index=False)
    print(f'Merged data saved to {output_file}')

# Specify the folder path containing CSV files
folder_path = 'result'

# Call the function to merge CSV files
merge_csv_files(folder_path)
