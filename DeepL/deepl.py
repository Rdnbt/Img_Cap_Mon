import requests
import csv

AUTH_KEY = "2c709567-3add-082d-a133-65f22d8bc4f5:fx"
translate_url = "https://api-free.deepl.com/v2/translate"

def translate_text(text):
    """
    Translates the given text from English to Mongolian using DeepL API.

    :param text: The text to be translated.
    :return: The translated text.
    """
    params = {
        "auth_key": AUTH_KEY,
        "text": text,
        "source_lang": "EN",
        "target_lang": "JP"
    }
    response = requests.post(translate_url, data=params)
    response_json = response.json()
    translated_text = response_json.get("translations", [{"text": ""}])[0]["text"]
    return translated_text

def translate_dataset(input_file, output_file):
    """
    Translates the captions in the dataset from English to Mongolian and saves the translated dataset.

    :param input_file: The path to the input dataset file in CSV format.
    :param output_file: The path to save the translated dataset file in CSV format.
    :return: None.
    """
    translated_rows = []

    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter='|')
        header = next(reader)  # Read and store the header row
        translated_rows.append(header)  # Add the header row to the translated rows

        for row in reader:
            image_name, comment_number, comment = [col.strip() for col in row]
            translated_comment = translate_text(comment)
            translated_row = [image_name, comment_number, translated_comment]
            translated_rows.append(translated_row)

    with open(output_file, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(translated_rows)

    print("Translation completed. Translated dataset saved at: {}".format(output_file))

# Provide the input and output file paths
input_file = "test_short.csv"
output_file = "translated_dataset.csv"

# Translate the dataset
translate_dataset(input_file, output_file)