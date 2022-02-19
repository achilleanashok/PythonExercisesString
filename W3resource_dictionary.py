
#Ex: Different ways to sort a dictionary
import operator


def sortdictbyvalue():
    #Initialize the dictionary
    my_dict = {2: 'three',
               1: 'two',
               0: 'azero'}
    sorted_dict = dict(sorted(
        my_dict.items(),
        key=lambda kv: kv[1],
        reverse = True
    ))
    print(my_dict)
    print(sorted_dict)
def sortdictbyvaluewithitems():
    my_dict = {'c': 3,
               'a': 1,
               'd': 4,
               'b': 2
    }
    sorted_dict = sorted([key, value]
                         for (key, value) in my_dict.items())
    print(my_dict)
    print(sorted_dict)

def sortdictbysortedandget():
    my_dict = {'red': '#FF0000',
               'green': '#008000',
               'black': '#000000',
               'white': '#FFFFFF'
    }
    for w in sorted(my_dict, key = my_dict.get):
        print(w, my_dict[w])

import operator
def sortdictbyitemgetterfromoperator():
    my_dict = {'a': 23, 'g': 67, 'e': 12, 45: 1
    }
    sorted_dict = sorted(my_dict.items(), key=operator.itemgetter(1))
    print(my_dict)
    print(sorted_dict)

from collections import OrderedDict
def sortdictbyordereddict():
    my_dict = {1: 2, 3: 4, 5: 6, 4: 3, 2: 1, 0: 0}

    sorted_dict = OrderedDict(sorted(
        my_dict.items(), key=lambda x: x[1]
    ))

    print(my_dict)
    print(sorted_dict)
sortdictbyvalue()