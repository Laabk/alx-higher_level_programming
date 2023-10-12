#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    resut = 0
    the_digt = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for a_rom in reversed(roman_string):
        the_arabic = the_digt[a_rom]
        rsut = resut + the_arabic if resut < the_arabic * 5 else -the_arabic
    return (resut)
