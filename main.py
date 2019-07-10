from textblob import TextBlob
import matplotlib.pyplot as plt
import sys,tweepy
#(sys)system specific parameters and fuctions. 
#This module provides access to some variables used or maintained by the 
#interpreter and to functions that interact strongly with the interpreter.

def percentage(part,whole):
    return 100*(part/whole)

consumer_key="QFKrr8B6Eb58nabiY1UbyLRJ5"
consumer_secret="2tmjZHmVyYYe0s87zJAT45IwpSxqcYqh8wSzTExD3J4J2iBSa6"
access_token="1147376671340691456-DSa5cdpWm9rJ3TZBNPJ93WI4Eqqe9r"
access_token_secret="9pZx4SfMQXGZXVQ1el5IDeWGWQxVQnjTS0omWn4YffnGl"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)#creating an OAuthHandler instance.
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth) 
#Creation of the actual interface, using authentication

search_term=input("Enter keyword to search about: ")
no_of_search_term=int(input("Enter how many tweets to analyze: "))

tweets=tweepy.Cursor(api.search,q=search_term,lang="English").items(no_of_search_term)#get all tweets about search term in english
#tweepy.Cursor(api.home_timeline,since=any date(2015-10-10),untill=any date)#without search term

positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    #print(tweet.text)
    analysis=TextBlob(tweet.text)
    #print(analysis.sentiment)
    polarity=polarity+analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0):
        neutral+=1
    elif(analysis.sentiment.polarity>0):
        positive+=1
    elif(analysis.sentiment.polarity<0):
        negative+=1

polarity=percentage(polarity,no_of_search_term)
positive=percentage(positive,no_of_search_term)
negative=percentage(negative,no_of_search_term)
neutral=percentage(neutral,no_of_search_term)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')

print("How people are reacting on " +search_term+ " by analysing " +str(no_of_search_term)+ " tweets,")
if(polarity==0):
    print("Neutral")
elif(polarity>0):
    print("Positive")
elif(polarity<0):
    print("Negative")

    
labels=['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
sizes=[positive,neutral,negative]
colors=['yellow','yellowgreen','red']
patches, texts = plt.pie(sizes, colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
#'best' for axes, 'upper right' for figures
plt.title("How people are reacting on " +search_term+ " by analysing " +str(no_of_search_term)+ " tweets,")
plt.axis('equal')
#if we have a circle in a graph then it looks circle if axis is equal otherwise it can be look like as ellipse.
plt.tight_layout()
#will adjust spacing between subplots to minimize the overlaps
plt.show()




