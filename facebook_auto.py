import facebook as fb
access_token = "EAAElfQepEBEBALEOO9ZBWtZAjO06fTtaAZCb87rxjIbDfqg00fzW6gwWyzGAN6hNvuYgMN5MyUZAU0YCmZC1YoOlBaFtBLu1ZCAqDxtAZBWEFMblij5kWigS2mp77BJOUrTF9ZBkCFDoA0hixx1uHli43fXypdNqCnT1iTbHHPIYa9SM3ZAuiZCCNTTdzebXtzFftvazbgvWm1cgZDZD"
asafb = fb.GraphAPI(access_token)
asafb.put_object("me", "feed", message="<video src='shoton.mp4'> </video> ")
# asafb.get_object("object id")

# asafb.put_photo(open("ME.webp", 'rb'), message="automatic photo posting")
# asafb.put_video(open("shoton.mp4", 'rb'), message="put video to tyest autoposting")
















# DOCS
# pip install facebook-sdk
# import facebook as fb

# # Get Access token - Follow the video on how to get access token for your fb account
# access_token = ""

# # The Graph API allows you to read and write data to and from the Facebook social graph
# asafb = fb.GraphAPI(access_token)

# # Post a message in the facebook page
# asafb.put_object("me","feed",message = "This is automated post!")

# # Get the contents of a post
# asafb.get_object("Page_ID_Obj_ID")

# # Post a photo with captions
# asafb.put_photo(open("meme.jpg","rb"), message = "Automated meme post")

# # Comment on a post
# asafb.put_object("Page_ID_Obj_ID","comments",message = "This is an automated comment!")

# Some sample API requests to get the data from facebook:

# Get Fan count for the page: 
# https://github.com/AbishekSA/Explained_In_Minutes/blob/main/Automate%20Facebook%20using%20python.ipynb