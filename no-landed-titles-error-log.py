import re

def extract_province_numbers(log_message):
    # Longer matching string to prevent mismatch. Also, it's regular expression, careful about that
    regex = r"Province '(\d+)' has no associated title in common\/landed_titles\." 
    matches = re.findall(regex, log_message)
    return matches

def format_province_list(province_numbers):
    formatted_list = []
    line_length = 10 # so that there's only 10 province IDs in a row
    for i in range(0, len(province_numbers), line_length):
        line = " ".join(province_numbers[i:i+line_length])
        formatted_list.append(line)
    return formatted_list

# Specify the path to the error log file
error_log_path = "C:\\Users\\L\\Documents\\Paradox Interactive\\Crusader Kings III\\logs\\error.log"

# Read the error log file
with open(error_log_path, "r") as file:
    error_log_content = file.read()

# Extract province numbers from the error log content
provinces = extract_province_numbers(error_log_content)

# Format the province numbers as a list with specified line length
province_list = format_province_list(provinces)

# Print the result
for line in province_list:
    print(line)
