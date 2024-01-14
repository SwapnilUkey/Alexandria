# Change the file paths as needed
input_file_path = 'catalog.json'
output_file_path = 'catalog.json'

# Reading the file in UTF-16
with open(input_file_path, 'r', encoding='utf-16') as file:
    data = file.read()

# Writing the file in UTF-8
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(data)
