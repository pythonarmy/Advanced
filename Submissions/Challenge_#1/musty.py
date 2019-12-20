import re

regex_integer_in_range = r'[^0]\d{5}$'
regex_alternating_repetitive_digit_pair =  r'(\d)(?=(\d)\1)'

def checkPostalCode(string):
    return (bool(re.match(regex_integer_in_range, string)) and len(re.findall(regex_alternating_repetitive_digit_pair, string)) < 2)

if __name__ == "__main__":
    print(checkPostalCode('123456')) # True

    print(checkPostalCode('110104'))  # False

    print(checkPostalCode('4372724')) # False
