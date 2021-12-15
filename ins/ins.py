# from instabot import Bot
 
 
# bot = Bot()
 
# bot.login(username = "hayotbekabdulazizov200",
#           password = "gafur22hayotbek")
 
# # Recommended to put the photo
# # you want to upload in the same
# # directory where this Python code
# # is located else you will have
# # to provide full path for the photo
# bot.upload_photo("img.jpg",
#                  caption ="Technical Scripter Event 2019")




# import hashlib
# from urllib.request import urlopen
 
# def readwordlist(url):
#     try:
#         wordlistfile = urlopen(url).read()
#     except Exception as e:
#         print("Hey there was some error while reading the wordlist, error:", e)
#         exit()
#     return wordlistfile
 
 
# def hash(wordlistpassword):
#     result = hashlib.sha1(wordlistpassword.encode())
#     return result.hexdigest()
 
 
# def bruteforce(guesspasswordlist, actual_password_hash):
#     for guess_password in guesspasswordlist:
#         if hash(guess_password) == actual_password_hash:
#             print("Hey! your password is:", guess_password,
#                   "\n please change this, it was really easy to guess it (:")
#             # If the password is found then it will terminate the script here
#             exit()
 
# ############# append the below code ################ 

# url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
# actual_password = 'henry'
# actual_password_hash = hash(actual_password)
 
# wordlist = readwordlist(url).decode('UTF-8')
# guesspasswordlist = wordlist.split('\n')
 
# # Running the Brute Force attack
# bruteforce(guesspasswordlist, actual_password_hash)
 
# # It would be executed if your password was not there in the wordlist
# print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")
 



# from instapy import InstaPy
  
# session = InstaPy(username="hayotbekabdulazizov200",password="gafur22hayotbek")
# session.login()
# session.like_by_tags(["dance", "mercedes"], amount=10, interact=True)
# session.set_dont_like(["naked", "murder", "nsfw"])
# session.set_do_comment(True, percentage=100)
# session.set_comments(["Nice", "Amazing", "Super"])
# session.set_do_follow(enabled=True, percentage=100)
# session.set_user_interact(amount=1, randomize=True, percentage=100)
# session.end()


