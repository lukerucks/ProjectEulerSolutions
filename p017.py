"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

under_twenty = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
under_twenty += ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def convert_int_to_string(number):
    if number == 0:
        return "zero"
    elif 1 <= number < 20:
        return under_twenty[number]
    elif 20 <= number < 100:
        tens_digit = int(str(number)[0])
        ones = number % 10
        return tens[tens_digit] + " " + under_twenty[ones]
    elif 100<= number < 1000:
        if number % 100 != 0:
            under_hundred_str = convert_int_to_string(number % 100)
            return under_twenty[int(str(number)[0])] + " hundred and " + under_hundred_str
        else:
            return under_twenty[int(str(number)[0])] + " hundred"
    elif 1000<=number<10000:
        if number % 1000 != 0:
            under_thousand_str= convert_int_to_string(number % 1000)
            return under_twenty[int(str(number)[0])] + " thousand " + under_thousand_str
        else:
            return under_twenty[int(str(number)[0])] + " thousand"




begin_str = ""
for number in range(1, 1001):
    number_in_words = convert_int_to_string(number)
    print number_in_words
    begin_str += number_in_words.replace(" ","")

print len(begin_str)



