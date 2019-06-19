import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tkinter import *



access_token="837336202432892930-m8KrjzsweI6iWmLfDVJfjxy5lQCj5Rs"
access_token_secret="Mksze0mFAruWB5slgc8Bzo6s4tEuyGpeptSXaIpYwWGiM"
consumer_key="k35UTG92SnmrvvTu8vq9E4UUx"
consumer_secret="1yIl33DbxMlFUkJu5rmvEbRBDEM2j3eMwtkos24Komvw0n0Lzz"



auth=tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)




def gettweet(event=None):
    global inpt,outpt
    z=inpt.get()
    if len(list(z))>1:
        s=list(map(str,z.split(',')))
    else:
        s=list(str(z))
    fetched_tweets = api.search(q=s, result_type='recent', lang='en', count=100,tweet_mode='extended')
    #fetched_tweets=api.trends_available(tweet_mode='extended')
    aa=str()
    num=0
    for tweet in fetched_tweets:
        num+=1
        user=str(tweet.author._json['screen_name'])
        char_list = [user[j] for j in range(len(user)) if ord(user[j]) in range(65536)]
        user=''
        for j in char_list:
            user=user+j
        aa+=" ( "+str(num)+" ) ["+str(tweet.created_at)+"] "+str(user)+" : "

        user=tweet.full_text
        char_list = [user[j] for j in range(len(user)) if ord(user[j]) in range(65536)]
        user=''
        for j in char_list:
            user=user+j
        aa+=user+"\n\n\n"
        
    outpt.config(state=NORMAL)
    outpt.delete('1.0','end')
    outpt.insert(INSERT,aa)
    outpt.config(state=DISABLED)




root=Tk()

root.resizable(0,0)

root.title("Know The Tweets")

label=Label(root,text="Enter the Topic ",background="sky blue",font='Helvetica 18 bold')

label.pack()

inpt=Entry(root,background="light yellow",font='Helvetica 18 bold')

inpt.bind('<Return>',gettweet)

inpt.pack()

btn1=Button(root,text="Search",background="sky blue",font='Helvetica 14 bold',command=gettweet)

btn1.pack()

outpt=Text(root,bd=1,borderwidth=5,font='Helvetica 18 bold',background="sky blue")

outpt.pack()

outpt.config(state=DISABLED)

outpt.config(wrap=WORD)

root.configure(background="sky blue")

root.mainloop()
