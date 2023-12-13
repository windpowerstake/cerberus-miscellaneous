import pandas as pd
import os

def combine_and_sum(file1_path, file3_path, output_path):
    # Read CSV files into pandas DataFrames
    df1 = pd.read_csv(file1_path)
    df3 = pd.read_csv(file3_path)

    # Check if the 'amount' columns exist in DataFrames
    if 'amount' not in df1.columns:
        print("Error: 'amount' column not found in file1.")
        return

    # Rename the 'amount' columns for clarity
    df1.rename(columns={'amount': 'amount_file1'}, inplace=True)

    # Merge DataFrames based on the 'address' column
    merged_df = pd.merge(df1, df3, left_on='address', right_on='addr', how='outer')

    # Fill NaN values with 0
    merged_df['amount_file1'].fillna(0, inplace=True)
    merged_df['shares'].fillna(0, inplace=True)

    # Combine the values from both files
    merged_df['combined_value'] = merged_df['amount_file1'] + merged_df['shares']


    # Sort DataFrame based on 'combined_value' column
    merged_df.sort_values(by='combined_value', ascending=False, inplace=True)

    # Filter out rows where 'combined_value' is less than 1000000
    merged_df = merged_df[merged_df['combined_value'] >= 1000000]

    # Save the result to a new CSV file
    merged_df.to_csv(output_path, index=False)

    # Post-process to convert 'cerberus' addresses to 'osmo' addresses and save to another file
    os.system(f'awk -F"," \'{{ cmd1 = "echo \\"\" $1 "\\" | bech32-convert -from cerberus -to osmo"; cmd1 | getline converted_addr; close(cmd1); cmd2 = "echo \\"\" $3 "\\" | bech32-convert -from cerberus -to osmo"; cmd2 | getline converted_third; close(cmd2); printf "%s,%s,%s,%s,%s,%s\\n", converted_addr, $2, converted_third, $4, $5, $6 }}\' {output_path} > osmo_output_osmo.csv')

# Example usage
file1_path = 'export_cerb_block_4574265v2.txt.csv'
file3_path = 'result_export_cerb_block_4574265v2.csv'
output_path = 'output_combined.csv'

combine_and_sum(file1_path, file3_path, output_path)

