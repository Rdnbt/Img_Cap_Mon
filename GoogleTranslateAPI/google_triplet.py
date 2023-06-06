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
        header = lines[0]  # Retrieve the header row

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|')

        # Write the header row to the output file
        header.append('Translated Comment')
        writer.writerow(header)

        for line in lines[1:]:
            image_name, comment_number, comment = line
            translated_comment = translate_text(comment, dest_language)

            # Append the translated Mongolian caption to the existing row
            line.append(translated_comment)
            writer.writerow(line)

# Example usage
input_file = 'test_short.csv'
output_file = 'output_short.csv'
destination_language = 'mn'  # Mongolian language code

translate_csv(input_file, output_file, destination_language)
