SMALL_NUMS = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
]

PREFIXES = [
    "twenty",
    "thirty",
    "fourty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]

THIRD_ORDERS = [
    "",
    " thousand",
    " million",
    " billion",
    " trillion",
    " quadrillion",
    " quintillion",
    " sextillion",
    " septillion",
    " octillion",
    " nonillion",
    " decillion"
]

FRACTIONAL_PREFIXES = [
    "",
    "ten",
    "hundred"
]

def starts_negative(number):
    if len(number) == 1:
        return "Invalid number"
    
    if number[1].isdigit():
        return starts_digit(number[1:], "negative ")
    elif number[1] == ".":
        return starts_decimal(number[1:], "negative ")
    else:
        return "Invalid number!"

def find_first_non_digit(starts_digit):
    for i, c in enumerate(starts_digit):
        if not c.isdigit():
            return i, c
    
    return -1, ""

def remove_extra_zeros(digits):
    for i, c in enumerate(digits):
        if not c.isdigit():
            break
        
        if c != "0":
            return digits[i:]
    
    return "0"

def starts_digit(number, prefix):
    end, non_digit = find_first_non_digit(number)
    
    if end == -1:
        end = len(number)
    
    digits = remove_extra_zeros(number[:end])
    decimal_engl = ""

    if non_digit == ".":
        decimal_engl = convert_decimals(number[end:])

        if digits == "0" and decimal_engl == "":
            return "zero"
    
    return convert_digits(digits) + decimal_engl

def convert_decimals(decimals):
    if len(decimals) == 1:
        return ""
    
    first_non_zero_digit = find_first_non_zero_digit(decimals[1:]) + 1

    if first_non_zero_digit == -1:
        return ""
    
    last_non_zero_digit = find_last_non_zero_digit( \
        decimals[first_non_zero_digit:]) + first_non_zero_digit
    digits = decimals[first_non_zero_digit:last_non_zero_digit + 1]
    engl = convert_digits(digits) + convert_decimal_place(last_non_zero_digit)

    if len(digits) > 1 or digits[0] != '1':
        engl += "s"
    
    return engl

def convert_decimal_place(place):
    prefix = FRACTIONAL_PREFIXES[place % 3]
    
    if prefix == "":
        engl = THIRD_ORDERS[place // 3]
    else:
        engl = " " + prefix

        if place > 2:
            engl += THIRD_ORDERS[place // 3]
    
    engl += "th"
    return engl

def find_last_non_zero_digit(digits):
    last_non_zero = 0

    for i, c in enumerate(digits):
        if not c.isdigit():
            break

        if c != "0":
            last_non_zero = i
    
    return last_non_zero

def find_first_non_zero_digit(digits):
    for i, c in enumerate(digits):
        if not c.isdigit():
            break
        
        if c != "0":
            return i

    return -1

def convert_digits(digits):
    first_group_len = len(digits) % 3
    
    if first_group_len == 0:
        first_group_len = 3

    third_order = (len(digits) - 1) // 3
    engl = convert_group(digits[:first_group_len], third_order)

    for i in range(0, third_order):
        start = first_group_len + i * 3
        group_engl = convert_group(digits[start:start + 3], third_order - i - 1)
        
        if group_engl != "":
            engl += " " + group_engl
    
    return engl

def convert_group(group, third_order):
    group_int = int(group)
    
    if group_int == 0:
        return ''
    elif group_int < 20:
        engl = SMALL_NUMS[group_int]
    else: 
        first_digit = int(group[0])

        if group_int < 100:
            second_digit = int(group[1])
            engl = PREFIXES[first_digit - 2]

            if second_digit != 0:
                engl += "-" + SMALL_NUMS[second_digit]
        else:
            engl = SMALL_NUMS[first_digit] + " hundred"
            remainder = convert_group(group[1:], 0)

            if remainder != "":
                engl += " " + remainder
    
    engl += THIRD_ORDERS[third_order]
    return engl

def starts_decimal(number, prefix):
    return ""

while True:
    number = input("Enter a number: ")

    if len(number) == 0:
        print("Invalid number!")
        continue

    if number[0] == "-":
        engl = starts_negative(number)
    elif number[0].isdigit():
        engl = starts_digit(number, "")
    elif number[0] == ".":
        engl = starts_decimal(number, "")
    else:
        engl = "Invalid number!"

    print(engl)