# SEPARATOR
from requests.api import request


def separator(item=None ,*items):
    """
        function thatr separate string or any type of data to integers and 
        strings and return two lists in one list [strings, integers] !!1 

        example:
        "a5g2g33mmn4"   returns [['a','g','g','m','m','n'], [5,2,3,3,4]]
    """
    strings = []
    integers = []

    for i in item:
        try:
            integers.append(int(i))
        except:
            strings.append(str(i))    
    return [strings, integers]



# REQUESTS 
def requester(url, method, *args, **kwargs):
    import requests
    pass





# PDF Translator 
def pdf_trans(url):
    try:
        pass
    except:
        pass






# calculates sleep time
time_ = str(input('Time >>>  '))
hour = time_.split(':')[0]
minute = time_.split(':')[1]
time_ = int(hour) + 7
if time_ > 24:
    time_ -= 24
print(f"{time_}:{minute}")





# wordfinder find word with index
def finder(*args):
    ls_of_letters = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return ''.join(ls_of_letters[x] for x in args)
# print(finder(1,19,1,13))