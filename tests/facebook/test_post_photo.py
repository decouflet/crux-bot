import unittest
import json
import sys
sys.path.append("C:/Users/Leonel/Documents/crux-bot")

import cruxbot.facebook_actions as fb
import cruxbot.utils.constant as constant


class ConversationMessagesTest(unittest.TestCase):

    def setUp(self):
        self.page_id = constant.PAGE_ID
        self.page_access_token = constant.PAGE_ACCESS_TOKEN

        self.api = fb.ExtApi(long_term_token = "long-term-token")


    def testPostPhoto(self):

        self.api.post_photo(
            page_id = self.page_id,
            access_token = self.page_access_token,
            files = open("images.jpg", 'rb'),
            return_json = True
        )

        data = []

        with open("data\\facebook\\fb_post_photo.json") as file:
            data = json.load(file)

        self.assertTrue("id" in data)
        self.assertTrue("post_id" in data)


if __name__ == "__main__":
    unittest.main()