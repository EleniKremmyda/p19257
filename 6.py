import tweepy

auth = tweepy.OAuthHandler(" ", " ")
auth.set_access_token(" ", " ")

api = tweepy.API(auth)

input_user = input("Enter the name of the account you want to search: ")
tweets = api.user_timeline(screen_name= input_user, count= 10, include_rts = False, tweet_mode = 'extended')

words = []
for tweet in tweets:

    #Get the tweet text.
    tweet_text = tweet.full_text
    tweet_text = tweet_text.split()

    #Get the words from the tweet.
    for word in tweet_text:
        #Append any word that isn't a link, or isn't a mention to another user.
        if not(word.startswith("http")) and not(word.startswith("@")):
            words.append(word)

for i, word in enumerate(words):
    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.replace('!', '')
    word = word.replace('?', '')
    word = word.replace('(', '')
    word = word.replace(')', '')

    if len(word) == 1:
        words.pop(i)

#Sort all the words (in ascending order) by their length
words = sorted(words, key=len)
words.reverse()

#Print the five longest words.
print("The five longest words, user " + input_user + " has tweeted, are:\n")
print(words[0])
print(words[1])
print(words[2])
print(words[3])
print(words[4])

words.reverse()

#Print the five shortest words.
print("\n\nThe five shortest words, user " + input_user + " has tweeted, are:\n")
print(words[0])
print(words[1])
print(words[2])
print(words[3])
print(words[4])
