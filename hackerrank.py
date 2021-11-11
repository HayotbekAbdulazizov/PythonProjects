# https://www.hackerrank.com/challenges/grading/problem      #LIKE SHEDEVR   integer rounder
"""
def round_numbers(item):
    final_numbers = []
    for x in item:
        if x >= 38:
            if str(x).endswith('3') or str(x).endswith('4') or str(x).endswith('5'):
                result = x + (5 - int(str(x)[-1]))
                final_numbers.append(result)
            elif str(x).endswith('8') or str(x).endswith('9') or str(x).endswith('10'):
                result_2 = x + (10 - int(str(x)[-1]))
                final_numbers.append(result_2)
            else:
                final_numbers.append(x)    
        else:
            final_numbers.append(x)       
    return final_numbers            
print(round_numbers([73,67,38,33]))
"""



