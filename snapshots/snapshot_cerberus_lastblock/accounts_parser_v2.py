import json
import csv


# Replace 'your_file_path' with the actual path to your JSON file
file_path = '/home/wind/Documents/export_cerb_lastblock_4849999.txt'

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
    # ... Add the rest of the excluded addresses
]

# Read the file line by line
with open(file_path, 'r') as file:
    # Concatenate lines until a complete JSON object is obtained
    json_content = ''
    for line in file:
        json_content += line.strip()
        if json_content.endswith('}'):
            break

# Parse the JSON content
data = json.loads(json_content)

# Check for the presence of 'app_state' and 'bank' keys
if 'app_state' in data and 'bank' in data['app_state']:
    # Extract address and amount data excluding the specified addresses
    rows = [
        (item['address'], item['coins'][0]['amount'])
        for item in data['app_state']['bank']['balances']
        if item['address'] not in excluded_addresses
    ]

    # Write to CSV file
    with open('export_cerb_lastblock_4849999_crosscheck.txt', 'w', newline='') as csvfile:
        fieldnames = ['address', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in rows:
            writer.writerow({'address': row[0], 'amount': row[1]})
else:
    print("Invalid JSON structure. Unable to extract 'app_state' or 'bank' information.")

