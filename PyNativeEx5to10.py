import re
# Ex 6: Create a mixed string using the following rules
def concat_string(s1, s2):

    len_s1 = len(s1)
    len_s2 = len(s2)
    result_string=""
    i, j = 0, len_s2 - 1
    while i < len_s1 and j >= 0:
        print(s1[i])
        print(s2[j])
        result_string = result_string + s1[i] + s2[j]
        i += 1
        j -= 1
    print(result_string)
    return result_string

# Ex 7: String characters balance Test
def string_balance_test(s1, s2):
    flag = True

    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


# Ex 8: Find all occurrences of a substring in a given string by ignoring the case
def find_all_occurences(s1, s2):

    len_s1 = len(s1) - 1
    len_s2 = len(s2)
    cnt = 0
    i = 0
    while i < len_s1:
        print(s1[i:i+len_s2])

        if s1[i:i+len_s2].lower() == s2.lower():
            cnt += 1
        i += 1
    return cnt


# Ex 8: Find all occurrences of a substring in a given string by ignoring the case
def find_all_occurences_pythonicway(s1, s2):
    return s1.lower().count(s2.lower())


#Ex 9: Calculate the sum and average of the digits present in a string
def tocalculate_sum_avg(s1):
    tot_sum = 0
    cnt = 0
    average = 0.0
    for char in s1:
        if char.isdigit():
            tot_sum += int(char)
            cnt += 1
    return tot_sum, tot_sum/cnt

import re
#Ex 9: Calculate the sum and average of the digits present in a string
def tocalculate_sum_avg_withregexp(s1):
    digit_list = [int(num) for num in re.findall(r'\d', s1)]
    print('Digits:', digit_list)
    # use the built-in function sum
    total = sum(digit_list)
    # average = sum / count of digits
    avg = total / len(digit_list)
    print("Sum is:", total, "Average is ", avg)

# Ex 10: Write a program to count occurrences of all characters within a string
def to_calculate_char_occurence(s1):
    char_dict = {}
    char_dict1 = dict()
    for char1 in s1:
        ct = s1.count(char1)
        char_dict1[char1] = ct
        if char1 not in char_dict:
            char_dict[char1] = 1
        else:
            char_dict[char1] += 1
    print(char_dict, char_dict1)
    return char_dict


# Ex 11: To reverse a given string
def toreverse_given_string(s1):
    len_s1 = len(s1) - 1
    i = 0
    result_str=""
    while len_s1 >= 0:
        result_str += s1[len_s1]
        len_s1 -= 1
    print(result_str)
    return result_str

    #return s1[::-1]
    #another way
    #return ''.join(reversed(s1))

# Ex 12: To find the last position of a string in a given string
def to_find_last_position(s1, s2):
    index = s1.rfind("Emma")
    print(index)
    #return index

    len_s1 = len(s1)
    len_s2 = len(s2)
    i = 0
    s3 = reversed(s1)
    while i < len_s1:
        if s3[i:i+len_s2].lower() == s2.lower():
            index1 = i
        i += 1
    return len_s1 - index1 - 1

# Ex 13: To find the count_chars_instring
def to_find_the_count_chars(stringtoformat):
    char_dict = dict()
    for chara in stringtoformat:
        if chara not in char_dict:
            char_dict[chara] = 1
        else:
            char_dict[chara] += 1
    str_format=""
    for keys, values in char_dict.items():
        str_format += keys+str(values)
    print(str_format)

def main():
    # Ex 6: Create a mixed string using the following rules
    # concat_string("Abc","Xyz")

    # Ex 7: String characters balance Test
    #print(string_balance_test("Ynf","PYnative"))

    # Ex 8: Find all occurrences of a substring in a given string by ignoring the case
    #print(find_all_occurences("Welcome to USA. usa awesome, isn't it?","usa"))
    #print(find_all_occurences_pythonicway("Welcome to USA. usa awesome, isn't it?", "usa"))

    # Ex 9: Calculate the sum and average of the digits present in a string
    # print(tocalculate_sum_avg("PYnative29@#8496"))

    # Ex 10: Write a program to count occurrences of all characters within a string
    #print(to_calculate_char_occurence("Apple"))

    # Ex 11: Reverse a given string
    #print(toreverse_given_string("PYnative"))

    # Ex 12: Find the last position of a given substring
    #print(to_find_last_position("Emma is a data scientist who knows Python. Emma works at google.","Emma"))

    # Facebook Questions:
    print(to_find_the_count_chars("I am back."))
if __name__ == "__main__":
    main()
