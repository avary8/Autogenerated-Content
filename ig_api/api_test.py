from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

folder = 'C:/Users/avamc_jl0do7/OneDrive - University of Florida/projects/ig_api/post_imgs/'
cl = Client()
cl.login(user, pw)

main = Client()
main.login(user, pw)

# media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CGgDsi7JQdS/')
# media_path = cl.video_download(media_pk)

# id = cl.user_info_by_username('tacc.8')
#print(id)

#get info by username. can look at other people not just who's logged in
# id = cl.user_info_by_username('avarymccormack')
# print(id)


print("\n----------liked posts from main-----------\n")

# main_liked = main.liked_medias(1)
# print(main_liked)

print("\n----------collection posts from main-----------\n")
#returns all collections info 
# collections = main.collections()
# print(collections)
main_collection = main.collection_medias_by_name(name='story')
print(main_collection[0])

# hashtag = cl.hashtag_info('dhbastards')

#return info about 20 medias (posts) from account
# media = cl.user_medias(id.pk, 20)
# print(media)

#delete post by pk 
# cl.media_delete(media[0].pk)

#upload photo
# media = cl.photo_upload(
#     folder+'20230615_1.jpg',
#     "First automated post",
# )

#upload vid to story 
# cl.video_upload_to_story(
#     media_path,
#     "Credits @adw0rd",
#     mentions=[StoryMention(user=adw0rd, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
#     links=[StoryLink(webUri='https://github.com/adw0rd/instagrapi')],
#     hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
#     medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)]
# )





