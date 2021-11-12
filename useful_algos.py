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