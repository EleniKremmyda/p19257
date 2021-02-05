import tweepy

auth = tweepy.OAuthHandler("QRXaiZwpnu1Qvn1D0ukSKBTzu", "C7WWoM6Mb1AFSeAR8PsKdfOYmWbluvnWogA6kQWeADJ5pWkWcS")
auth.set_access_token("1349718097243082753-D7KW9RGBdHtD98fWt6HY33mlpASgAx", "cCzRXJrCHQ6xezPMtOcL2csvfzhQecFC9XVTNWYIP9z2R")

api = tweepy.API(auth)

input_user = input("Enter the name of the account you want to search: ")
tweets = api.user_timeline(screen_name= input_user, count= 10, include_rts = False, tweet_mode = 'extended')

longest_word = ""
for tweet in tweets:
  tweet_text = tweet.full_text
  tweet_text = tweet_text.split()
  for word in tweet_text:
    if len(word) > len(longest_word) and not(word.startswith("http")) and not(word.startswith("@")):
       longest_word = word

print(longest_word)
