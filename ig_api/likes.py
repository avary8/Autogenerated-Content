from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

main = Client()
main.login(user, pw)




print("\n----------liked posts from main-----------\n")

main_liked = main.liked_medias(1)
print(main_liked)































