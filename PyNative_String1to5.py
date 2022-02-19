

# Exercise 1A: Create a string made of the first, middle and last character

def appendstringfirstmidlast(strtoprocess):
    # edge case:
    len_str = len(strtoprocess)

    if len_str == 0:
        return 0
    elif 1 <= len_str <= 3:
        return strtoprocess
    else:
        return strtoprocess[0] + strtoprocess[int(len_str/2)] + strtoprocess[-1]


def appendstringfirstmidlastoriginal():
    str1 = 'James'
    print("Original String is", str1)

    # Get first character
    res = str1[0]

    # Get string size
    l = len(str1)
    # Get middle index number
    mi = int(l / 2)
    # Get middle character and add it to result
    res = res + str1[mi]

    # Get last character and add it to result
    res = res + str1[l - 1]

    print("New String:", res)

#print(appendstringfirstmidlast("James"))


# Exercise 1B: Create a string made of the middle three characters
def getstringmadeofmiddle3chars(strtoprocess):

    # get the length of the string
    len_str = len(strtoprocess)
    mid_str = int(len_str/2)
    if len_str == 0:
        return 0
    elif 1 >= len_str <= 3:
        return strtoprocess
    else:
        return strtoprocess[mid_str-1:mid_str+2]

print(getstringmadeofmiddle3chars("JaSonAy"))