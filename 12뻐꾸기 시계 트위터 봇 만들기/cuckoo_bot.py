import tweepy
import datetime
import threading

def check_time(curr_hour):
    dt=datetime.datetime.now()

    if curr_hour!=dt.hour:
        print(dt)
        curr_hour=dt.hour

        consumer_key="" #자신의 consumer_key
        consumer_secret="" #자신의 consumer_secret

        auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

        access_token="" #독자의 access_token
        access_token_secret="" #독자의 access_token_secret
        auth.set_access_token(access_token, access_token_secret)

        api=tweepy.API(auth)

        hour=0

        if curr_hour==0:
            hour=24
        else:
            hour=curr_hour
        tweet="@seanlab"
        for i in range(0,hour):
            tweet+='뻐꾹'
        
        api.update_status(status=tweet)

        print("Successfully Posted.")

    threading.Timer(1,check_time,args=[curr_hour]).start()

if __name__=='__main__'
    check_time(-1)