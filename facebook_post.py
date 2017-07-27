import facebook

import config

class FacebookPost(object):
    def __init__(self, token):
        self.token = token
        self.client = facebook.GraphAPI(token)

    def post_photo_to_group(self, group_id, image_path, caption=''):
        image = open(image_path, 'rb')

        post_path = "{0}/photos".format(group_id)
        return self.client.put_photo(image, post_path, caption=caption)

    def post_message_to_group(self, group_id, message, link=''):
        return self.client.put_object(str(group_id), 'feed',
                message=message,
                link=link)

def main():
    fb_client = FacebookPost(config.USER_ACCESS_TOKEN)
    for group_id in config.GROUP_IDS:
        print group_id
        if config.POST_IMAGE and config.IMAGE_PATH:
            fb_client.post_photo_to_group(group_id, config.IMAGE_PATH,
                    config.IMAGE_CAPTION) 
            print 'Posted photo to group id: {0}'.format(group_id)

        if config.POST_MESSAGE and config.MESSAGE:
            fb_client.post_message_to_group(group_id, config.MESSAGE, config.MESSAGE_LINK)
            print 'Posted message to group id: {0}'.format(group_id)


if '__main__' == __name__:
    main()
