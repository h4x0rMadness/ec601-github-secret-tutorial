import unittest
import twitter_example


class MyTestCase(unittest.TestCase):
    def test_fetch_successful(self):
        """
        test
        :return:
        """
        ck = 'rllmb3xW0SYqmv0f1fZok9q8T'
        cs = 'w69Hk40uV9O25DjOGO36in4E4pqPpZbHASZogbB9gHfzv4r87s'
        at = '1171844680603951104-htwoGiQZFbtEAR07GHcNmfOSQlagNi'
        ats = 'W89apGxuxGBHX7XWL49klJQlotzGCvOychsdrovONyJiB'

        res = twitter_example.fecth_random_tweets(ck, cs, at, ats)

        txt = []
        for tweet in res:
            txt.append(tweet.text)



        self.assertEqual(1, len(txt))


    def test_empty_with_wrong_key(self):
        """
        Test with wrong keys, catch the exception and assert if as expected
        :return:
        """
        ck = 'wrongkey'
        cs = 'wrongkey'
        at = 'wrongkey'
        ats = 'wrongkey'

        res = twitter_example.fecth_random_tweets(ck, cs, at, ats)
        try:
            for tweet in res:
                print(tweet)
        except Exception as e:
            print("exception condition")
            self.assertTrue(e, "Twitter error response: status code = 401")

        # self.assertTrue(twitter_example.fecth_random_tweets(ck, cs, at, ats) == 401)

        ##self.assertTrue(res.__sizeof__() == 0)


if __name__ == '__main__':
    unittest.main()
