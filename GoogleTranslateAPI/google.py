import csv
from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

def translate_csv(input_file, output_file, dest_language):
    with open(input_file, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        lines = list(reader)

    with open(output_file, 'w') as file:
        writer = csv.writer(file, delimiter='|')
        for line in lines:
            image_name, comment_number, comment = line
            translated_comment = translate_text(comment, dest_language)
            writer.writerow([image_name, comment_number, translated_comment])

# Example usage
input_file = 'test_short.csv'
output_file = 'output_short.csv'
destination_language = 'mn'  # Mongolian language code

translate_csv(input_file, output_file, destination_language)