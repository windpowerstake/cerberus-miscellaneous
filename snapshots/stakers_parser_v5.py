import os
import re
import csv

# File paths
input_file_path = '/home/wind/Documents/export_cerb_block_4574265.txt'
input_file_name = os.path.basename(input_file_path)
preprocessed_file_path = f'/home/wind/Documents/preprocessed_{input_file_name}'
output_file_path = f'result_{os.path.splitext(input_file_name)[0]}.csv'

# List of excluded addresses
# List of excluded addresses
excluded_addresses = [
    "cerberus1krc59rqye9ptzurkyuccu6ykse895m9cfwv956",
    "cerberus140l6y2gp3gxvay6qtn70re7z2s0gn57zs7ndn2",
    "cerberus1xwazl8ftks4gn00y5x3c47auquc62ssuevxnnm",
    "cerberus1lxz6ucd5qydhpwtpatn9wu83fc002v087guacf",
    "cerberus1tat2cy3f9djtq9z7ly262sqngcarvaktk7yeah",
    "cerberus1gp957czryfgyvxwn3tfnyy2f0t9g2p4pe2d8ll5e13",
    "cerberus1kdqjzvznnufaykuwpu2glu9g33jshw8wlnvx2a5e13",
    "cerberus1r34mlqewsxrde38vp3tzwh3rk5vt6ez09wgmkz5e13",
    "cerberus1l6kfy4xvy0a34fseyhvc6f6k8asukfdzjysdpk5e13",
    "cerberus1eckdsantax0n29y7lc7ctjyzrxsfkk5hh3a7e45e13",
    "cerberus1td92z5qwl39f407gxf6lu2x80enat7t38cnwfh5e13",
    "cerberus1y3thykrje2fmdcf8wva8l8kphmwpx89ukyny605e13",
    "cerberus13jawsn574rf3f0u5rhu7e8n6sayx5gkwwtq2rg5e13",
    "cerberus1g3d36rfxfqtlnz3hzd05cs2wrjgykcz2atlz8e5e13",
    "cerberus1u36xktpyrp6cw99a2e3up4jntn0e0zdm6fzxpk5e13",
    "cerberus1evv5y2ake002n9l27t5qhqcwhgwd6up2wmwsz65e13",
    "cerberus1uvl2g9nd8qttjjyxjs30x7fj878d3wt426l4x75e13",
    "cerberus1js6gk7q0vw2q8t2frsqcjl3s5tvlguqk9z2jrs5e13",
    "cerberus10ypajp3q5zu5yxfud3ayd95th0k7467kyp7tdq5e13",
    "cerberus13uz8x0rgm950639yklqq5tnjh6gwfpfhft5r7g5e13",
    "cerberus1fl48vsnmsdzcv85q5d2q4z5ajdha8yu3fufxvu",
    "cerberus1mey5jxekxeat0ptryhxq2qrpnc4pxpm9k7z9wx",
    "cerberus1jv65s3grqf6v6jl3dp4t6c9t9rk99cd8mcy4u5",
    "cerberus1kq2rzz6fq2q7fsu75a9g7cpzjeanmk685z9kwl",
    "cerberus1tygms3xhhs3yv487phx3dw4a95jn7t7lau4h6g",
    "cerberus1p6ea5azz4m96pkh7hxa34tw0d7pd2da7r4llwy",
    "cerberus1defc3wwn5z3jk5zwsv5mg49dcamdvz89rs2k7r",
    "cerberus10zwf7p04axrn4jn7n25pam4yjuxwjvuqp6v7kf",
    "cerberus1n55yq23pwjyuq3w29dj03eq249y07kpna5sh96",
    "cerberus1s8462924rzrmgs50hptk9c96qd3ap8zxkcn9yf",
    "cerberus1urr9m9hkkxmlrky2x3drjt5khhmzxlshs0tgh6",
    "cerberus1d8s9uzw2vpa5rk3n82l3tz9phd382xr8ze5e3c",
    "cerberus1whhx6h2nu4ywqyhqjdhezld5hyle77n5qccf6w",
    "cerberus1dtq0y9reqst7d99fd3c7x6dflh4eazm4t68f4u",
    "cerberus1xx0g3dl0dhu6kmxfdxek4n4dfdanvq3lyyt25m",
    "cerberus164nmq8ugvhy4wgesp848r0hl0m34akt5damnus"
]

# Use os.system to execute the shell commands
os.system(f"sed 's/delegator_address/\\n/g' {input_file_path} | sed '1d' | grep 'shares' > {preprocessed_file_path}")

# Regular expression to extract address and shares
pattern = re.compile(r'"(cerberus[^"]*)","shares":"([^"]*)"')

# Dictionary to store address as key and sum of shares as value
address_shares = {}

# Read data from the preprocessed file
with open(preprocessed_file_path, 'r') as file:
    data = file.read()

# Extract address and shares using regular expression
matches = pattern.findall(data)
for match in matches:
    address, shares = match
    shares = float(shares)
    
    # Skip excluded addresses
    if address in excluded_addresses:
        continue
    
    if address in address_shares:
        address_shares[address] += shares
    else:
        address_shares[address] = shares

# Write the result to a CSV file
with open(output_file_path, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["addr", "shares"])
    for address, total_shares in address_shares.items():
        csvwriter.writerow([address, total_shares])

# Optionally, remove the intermediate preprocessed file
os.remove(preprocessed_file_path)

