import re

def extract_province_numbers(log_message):
    regex = r"Province '(\d+)' has no associated title in common/landed_titles."
    matches = re.findall(regex, log_message)
    return matches

def format_province_list(province_numbers):
    formatted_list = []
    line_length = 20
    for i in range(0, len(province_numbers), line_length):
        line = " ".join(province_numbers[i:i+line_length])
        formatted_list.append(line)
    return formatted_list

# Example error log message
error_log = "[14:39:02][landedtitlemanager.cpp:980]: Province '11957' has no associated title in common/landed_titles. FIX THIS. Game will probably crash if you don't"

# Extract province numbers from the error log message
provinces = extract_province_numbers(error_log)

# Format the province numbers as a list with specified line length
province_list = format_province_list(provinces)

# Print the result
for line in province_list:
    print(line)
