import requests
import uuid
import json
import csv

# Add your key and endpoint
key = "c09e68d39c864550a5a6f5f61f5432fb"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Location, also known as region.
# Required if you're using a multi-service or regional (not global) resource.
# It can be found in the Azure portal on the Keys and Endpoint page.
location = "japaneast"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['mn']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # Location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# Input and output location 
input_file_path = 'test_short.csv'
output_file_path = 'output_Azure.csv'


# Open the input CSV file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file, delimiter='|')

    # Open the output CSV file
    with open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file, delimiter='|')

        # Process each row in the input file
        for row in reader:
            image_name, comment_number, comment = row

            # Skip the header row
            if comment_number == ' comment_number':
                writer.writerow(row)
                continue

            # Set the text to be translated
            body = [{'text': comment}]

            # Send translation request
            request = requests.post(constructed_url, params=params, headers=headers, json=body)
            response = request.json()

            # Extract the translated text from the response
            translated_text = response[0]['translations'][0]['text']

            # Write the translated row to the output file
            translated_row = [image_name, comment_number, translated_text]
            writer.writerow(translated_row)

print("Translation complete. Translated file saved to:", output_file_path)
