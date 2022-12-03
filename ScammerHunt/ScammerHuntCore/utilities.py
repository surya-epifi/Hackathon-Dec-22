import re

def get_phone_number(text):
    result = []
    numbers = re.findall(r'(?:\+\s*\d{2}[\s-]*)?(?:\d[-\s]*){10}', text)
    for number in numbers:
        number = ''.join(number.split())
        result.append(number[-10:])
    return result

# testing
# numbers = get_phone_number("I recieved a message from +91 81471 21834 for Bescom payment and asked me to install team viewer quicksupport to take control of my phone. This seems to be a fraud")
# print(numbers)