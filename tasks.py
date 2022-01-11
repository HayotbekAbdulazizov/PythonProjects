# # from math import radians
# # import random
# # ls_of_numbers = []
# # for i in range(3 , 999):
# #     ls_of_numbers.append(i)

# # numbers = random.sample(ls_of_numbers, 52)

# # def card_game(cards):
# #     vasya_list = []
# #     petya_list = []
# #     for i in range(len(cards)):
# #         if len(cards) == 0:
# #             return [vasya_list, petya_list]
# #         else:
# #             vasya =  random.choice(cards)
# #             vasya_list.append(vasya)
# #             cards.remove(vasya)
# #             if len(cards) != 0:
# #                 petya = random.choice(cards)
# #                 petya_list.append(petya)
# #                 cards.remove(petya)
            
# #                 if vasya < petya:
# #                     if len(cards) != 0:
# #                         vasya_2 = random.choice(cards)
# #                         vasya_list.append(vasya_2)
# #                         cards.remove(vasya_2)
# #                 else:
# #                     if len(cards) != 0:
# #                         petya_2 = random.choice(cards)
# #                         petya_list.append(petya_2)
# #                         cards.remove(petya_2)

# #     # return [vasya_list , petya_list]

# # result = card_game(numbers)

# # print('Vasya', len(result[0]))
# # print(result[0])
# # print('==========================')
# # print('Petya', len(result[1]))
# # print(result[1])

# # if len(result[0]) > len(result[1]):
# #     print('Petya is the Winner')
# # else:
# #     print('Vasya is the Winner')









# ##  Exam

# # boolls = 'false'
# # print(bool)

# # sdfg = 5 * '50'
# # print(sdfg)

# # print(IsDigit(8))
# # s = 'Nike Company'
# # print(s[1:3])

# # from random import random
# # print(random())

# # n = 12.98523
# # print(round(n, 2))
# from random import random
# import time
# from warnings import filters

# def func_for(ls):
#     result = 0
#     for i in ls:
#         result += i
#     return result  

# def func_while(ls):
#     i = 0
#     result = 0
#     while i < len(ls):
#         result += ls[i]
#         i += 1 
#     return result    

# def getSum(piece):
#     if len(piece)==0:
#         return 0
#     else:
#         return piece[0] + getSum(piece[1:]) 

# # print(getSum([1, 3, 4, 2, 5]))

# def arrayTog(ls1, ls2):
#     return ls1 + ls2

# def max_num(ls):
#     result = ''
#     ls.sort()
#     ls.reverse()
#     for i in ls:
#         result += str(i)
#     return int(result)

# print()

# def task_5(num):
#     ls_of_nums = [x for x in range(num)]
#     ls_of_f = []
#     print(ls_of_nums)
#     for i in ls_of_nums:
#         try:
#             ls_of_f.append(ls_of_f[i-1] +ls_of_f[i-2])
#         except:
#             ls_of_f.append(i)            

#     return ls_of_f

# # print(task_5(100))

# import random
# def task_6():
#     ls_of_res = []
#     ls = [x for x in range(10)]
#     for x in range(10):  
#         rand_nums = random.sample(ls, 2)
#         result = str(rand_nums[0]) + str(rand_nums[1])
#         first_num = round(int(result))
#         second_num = 100-first_num    
#         rand_nums_2 = 0
#         print(second_num)
#         print(first_num)
#         print('================')
#         while rand_nums_2 != second_num:
#             rand_n = [random.choice(ls), random.choice(ls)]
#             # rand_n = random.sample(ls, 2)
#             rand_nums_2 = int(str(rand_n[0]) + str(rand_n[1]))
#             print(rand_nums_2)
#             time.sleep(0.09)
#         ls_of_res.append([first_num, second_num])    

#     return ls_of_res


# print(task_6())





