from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import pandas as pd
import os

main = Client()
main.login(user, pw)

currType = ''
saveFolder = './saved/'

saved_df = pd.read_csv('./saved.csv')



def getPostType(media_type, product_type):
    if media_type == 1:
        return "photo"
    if media_type == 8:
        return "album"
    if media_type == 2:
        if product_type == 'feed':
            return "video"
        if product_type == 'clips':
            return "reel"
        return product_type


def downloadByType(currType, saveFolder, post):
    savePath = saveFolder + currType
    if currType == 'photo': 
        main.photo_download(post.pk, savePath)
        return
    if currType == 'video': 
        main.video_download(post.pk, savePath)
        return 
    if currType == 'reel': 
        main.clip_download(post.pk, savePath)
        return 
    if currType == 'igtv': 
        main.igtv_download(post.pk, savePath)
        return
    if currType == 'album': 
        os.makedirs(savePath + '/' + post.pk)
        #save all photos from an album in specific folder
        main.album_download(post.pk, savePath + '/' + post.pk)
        return
        


# print("\n----------collection posts from main-----------\n")
#---------------returns all collections info 
# collections = main.collections()
# print(collections)

# ----------write collection names to txt file-------------

# with open('./valid_collection.txt', "w", encoding='utf-8') as f:
#     for i in collections:
#         f.write(i.name+'\n')


curr_collec = 'TO POST'
curr_collec_pk = main.collection_pk_by_name(curr_collec)
main_collection = main.collection_medias(collection_pk=curr_collec_pk, amount = 0) #return all media

#print(main_collection[2])

# download reel 
# main.clip_download(main_collection[2].pk, saveFolder)


# photo : media_type = 1
# video : media_type = 2 : product_type = feed 
        # video clip link - 

# IGTV : media_type = 2 : product_type = igtv
# Reel : media_type = 2 : product_type = clips
# Album : media_type = 8



# add to csv of saved stuff. include collection name, post's pk , id, media_type , and product_type


# check to see if things already exist and then stop downloading after that value. 


#checking metadata .
print('user pk: ' + str(main_collection[0].user.pk))
# print('post pk: ' + str(main_collection[0].pk))
# print('post id: ' + str(main_collection[0].id))
# print('type: ' + getPostType(main_collection[0].media_type, main_collection[0].product_type))
# print('media type: ' + str(main_collection[0].media_type))
# print('prod type: ' + str(main_collection[0].product_type))
# print('fileName: ' + str(main_collection[0].user.username + main_collection[0].pk))



new_entry = {'collection name':curr_collec,'collection pk':curr_collec_pk,'user id':-1, 'post pk':-1,'post id':-1,'filepath':"",'type': "",'media_type':-1,'product_type':-1,'times posted':0, 'last time posted':""}

j = 0
for post in main_collection:
    j = j+1
    if post.pk in saved_df['post pk'].values:
        break
    currType = getPostType(post.media_type, post.product_type)
    new_entry['user id'] = post.user.pk
    new_entry['post pk'] = post.pk
    new_entry['post id'] = post.id
    new_entry['filepath'] = saveFolder + currType + '/' + post.user.username + post.pk
    new_entry['type'] = currType
    new_entry['media_type'] = post.media_type
    new_entry['product_type'] = post.product_type
    
    saved_df.loc[len(saved_df.index),:] = new_entry
    if currType == 'album':
        new_entry['filepath'] = saveFolder + currType + '/' + post.pk + '/' + post.user.username + post.pk
    downloadByType(currType, saveFolder, post)

print(j)
    
saved_df.to_csv('./saved.csv', index=False)
    


























