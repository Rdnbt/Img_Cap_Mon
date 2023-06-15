import csv
from googletrans import Translator

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        print("Translation error:", e)
        return ""

def translate_csv(input_file, output_file, dest_language):
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='|')
        lines = list(reader)
        header = lines[0]  # Retrieve the header row

    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')

        # Write the header row to the output file
        header.append('Translated Comment')
        writer.writerow(header)

        for line in lines[1:]:
            image_name, comment_number, comment = line
            translated_comment = translate_text(comment, dest_language)

            # Append the translated comment to the existing row
            line.append(translated_comment)
            writer.writerow(line)

# Example usage
input_file = 'output_1000.csv'
output_file = 'triplet_1000.csv'
destination_language = 'mn'  # Mongolian language code

translate_csv(input_file, output_file, destination_language)
