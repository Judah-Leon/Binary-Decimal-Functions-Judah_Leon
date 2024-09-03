def binary_to_decimal(binary_str: str) -> int:
    decimal_value = 0
    power = 0
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_value += 2 ** power
        power += 1
    return decimal_value

def decimal_to_binary(decimal_num: int) -> str:
    binary_str = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2
    binary_str = binary_str.zfill(8)
    return binary_str
