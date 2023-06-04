import random

def random_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    time_string = f"{hour:02d}:{minute:02d}:{second:02d}"
    return time_string

def random_province_number():
    return random.randint(1, 10000)

def error_string():
    time = random_time()
    number = random_province_number()
    text1 = "[landedtitlemanager.cpp:980]: Province"
    text2 = "has no associated title in common/landed_titles. FIX THIS. Game will probably crash if you don't"
    formatted_string = f"[{time}]{text1} '{number}' {text2}"
    return formatted_string

# [14:39:02][landedtitlemanager.cpp:980]: Province '11957' has no associated title in common/landed_titles. FIX THIS. Game will probably crash if you don't

print(error_string())
