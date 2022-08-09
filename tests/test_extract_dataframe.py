import unittest
import pandas as pd
import sys, os

sys.path.append(os.path.abspath(os.path.join("../Twitter-Data-Analysis")))

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below
sampletweetsjsonfile = "./tests/global_twitter_test_data.json"   #put here the path to where you placed the file e.g. ./sampletweets.json. 
_, tweet_list = read_json(sampletweetsjsonfile)

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    def test_find_statuses_count(self):
        self.assertEqual(
            self.df.find_statuses_count(),[107188, 48446, 365, 5831, 3865]
        )

    def test_find_full_text(self):
        text = [
            "RT @CGMeifangZhang: Chinese ambassador to the US has detailed why #USA House Speaker Nancy #Pelosi's visit to #Taiwan was opposed by #China\u2026",
            "RT @CGMeifangZhang: #Latest When the PLA conducted massive drills around #Taiwan in response to the serious provocations made by the US on\u2026",
            "Wilson Chinonso Blog: Nigerian tribes, the list and facts https://t.co/E58nxeVz0j \n\n#China #ChinaTaiwan #ManUnited",
            "RT @IndoPac_Info: A good infographic of #China's missile launches on #Taiwan on August 4th.\n\n#ChinaTaiwanCrisis https://t.co/STzRr9fhU5",
            "RT @shen_shiwei: Roger Waters: \"They're (Chinese) not encircling #Taiwan, Taiwan is part of China, and that's been absolutely accepted by t\u2026"

        ]

        self.assertEqual(self.df.find_full_text(), text)

    # def test_find_sentiments(self):
    #     print(f"5 sentiments: {self.df.find_sentiments(self.df.find_full_text())}")

    #     self.assertEqual(
    #         self.df.find_sentiments(self.df.find_full_text()),
    #         (
              
    #         ),
    #     )


    def test_find_screen_name(self):
        name = ['jmarzola1', 'xuejianosaka', 'wilson_chnns', 'ZIisq', 'Aurora20288302']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        f_count = [213, 45242, 28, 65, 9]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        friends_count =[877, 1505, 265, 272, 178]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), [])


    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main()

