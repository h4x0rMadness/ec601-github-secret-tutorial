import unittest
import twitter_example
import os


class MyTestCase(unittest.TestCase):
    def test_fetch_successful(self):
        """
        test
        :return:
        """
        at = os.getenv('ACCESS_TOKEN')
        ats = os.getenv('ACCESS_TOKEN_SECRET')
        ck = os.getenv('CONSUMER_KEY')
        cs = os.getenv('CONSUMER_SECRET')

        self.assertEqual("1171844680603951104-HkluSJhInuGyqhdK6Xz1sTpnRB0y7e", at)
        self.assertEqual("aZWP7SsoRda3zWPYxH5yRDUSxLioWvtpKvFar8UR2kKl2", ats)
        self.assertEqual("rllmb3xW0SYqmv0f1fZok9q8T", ck)
        self.assertEqual("w69Hk40uV9O25DjOGO36in4E4pqPpZbHASZogbB9gHfzv4r87s", cs)


        res = twitter_example.fecth_random_tweets(ck, cs, at, ats)

        txt = []
        for tweet in res:
            txt.append(tweet.text)
        print(txt)


        self.assertEqual(1, len(txt))




if __name__ == '__main__':
    unittest.main()
