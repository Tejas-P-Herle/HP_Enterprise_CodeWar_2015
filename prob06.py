ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
one_to_twenty = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]
tens = [None, "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"]
powers_of_ten = ["hundred", "thousand", "lakh", "crore"]

def main():
    number = list(input())
    power_of_ten = 0
    number_in_words = ones[int(number[-3]) - 1] + " hundred " + parse_number_group(number[-2:])
    number = number[:-3]
    for i in range(len(number) - 2, -1, -2):
        power_of_ten += 1
        number_in_words = parse_number_group([number[i], number[i+1]], power_of_ten) + " " + number_in_words

    if len(number) % 2 != 0:
        number_in_words = parse_number_group([number[0]], power_of_ten + 1) + " " + number_in_words

    print(number_in_words.title())
        

def parse_number_group(digits, power_of_ten=None):

    if power_of_ten:
        return parse_twenties(digits) + " " + powers_of_ten[power_of_ten] + ("s" if int("".join(digits)) > 1 and power_of_ten != 1 else "")
    else:
        return parse_twenties(digits)

def parse_twenties(digits):

    len_digits = len(list(str(int("".join(digits)))))
    
    if len_digits == 1:
        return ones[int(digits[-1]) - 1]

    if len_digits == 2:
        if digits[0] == "1":
            return one_to_twenty[int(digits[-1]) - 1]
        return tens[int(digits[-2]) - 1] + " " + ones[int(digits[-1]) - 1]
    
if __name__ == "__main__":
    main()