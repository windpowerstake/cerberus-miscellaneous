import pandas as pd


def combine_and_average(file1_path, file2_path, output_path):
    # Read CSV files into pandas DataFrames
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Check if the 'amount' columns exist in DataFrames
    if 'amount (ucrbrus)' not in df1.columns or 'amount (ucrbrus)' not in df2.columns:
        print("Error: 'amount' column not found in one or both files.")
        return

    # Rename the 'amount' columns for clarity
    df1.rename(columns={'amount (ucrbrus)': 'amount_file1'}, inplace=True)
    df2.rename(columns={'amount (ucrbrus)': 'amount_file2'}, inplace=True)

    # Merge DataFrames based on the 'address' column
    merged_df = pd.merge(df1, df2, on='address', how='outer', suffixes=('_file1', '_file2'))

    # Fill NaN values with 0 and calculate average quantity
    merged_df['amount_file1'].fillna(0, inplace=True)
    merged_df['amount_file2'].fillna(0, inplace=True)
    merged_df['average_quantity'] = (merged_df['amount_file1'] + merged_df['amount_file2']) / 2

    # Add a column to specify from which file the entry came
    merged_df['source'] = merged_df.apply(lambda row: 'both' if row['amount_file1'] > 0 and row['amount_file2'] > 0 else ('file1' if row['amount_file1'] > 0 else 'file2'), axis=1)

    # Save the result to a new CSV file
    merged_df.to_csv(output_path, index=False)	


# Example usage
file1_path = '/home/wind/Documents/exports/export_cerb_block_4574265.txt.csv'
file2_path = '/home/wind/Documents/exports/export_cerb_lastblock_4849999.txt.csv'
output_path = 'output_combined.csv'

combine_and_average(file1_path, file2_path, output_path)
