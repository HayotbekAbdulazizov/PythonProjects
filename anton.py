# def ant(item):
#     word = 'anton'
#     result = []
#     if len(item) >= len(word):
#         for i in item:
#             if i in word and i not in result:
#                 result.insert(word.index(i), i)
#     return result

# print(ant(input(' >>> ')))





def ant(item):
    result = ''
    word = 'anton'
    if len(item) >= len(word):
        for i in word:
            for x in item:
                if x == i:
                    result += x
    return result



print(ant(input(' >>> ')))