#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import binascii

def binary_to_string(binary: str) -> str:
    """
    Write a function that takes in a binary string
    and returns the equivalent decoded text
    (the text is ASCII encoded).

    Each 8 bits on the binary string represent
    1 character on the ASCII table.

    The input string will always be a valid binary string.

    Characters can be in the range from "00000000"
    to "11111111" (inclusive)

    Note: In the case of an empty binary string your
    function should return an empty string

    How to convert binary string to and from ASCII text in Python:
    https://kite.com/python/answers/how-to-convert-binary-string-to-and-from-ascii-text-in-python
    https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

    :param binary:
    :return:
    """

    if not binary:
        return ''

    binary_int = int(binary, 2)
    byte_number = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    
    return ascii_text
