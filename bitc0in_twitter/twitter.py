# Provides twitter api functionality.

import tweepy


class Twitter:
    def __init__(self, *, key, secret, token, token_secret):
        # Preparing OAuth authentication
        self.auth = tweepy.OAuthHandler(key, secret)
        self.auth.set_access_token(token, token_secret)

        # Creating API interface
        self.api = tweepy.API(self.auth)

        # Creates a connection to the users profile
        self.user = self.api.me()
