#트위터로부터 인가를 획득하고, 트윗을 포스트하고, 타임라인을 읽어오는 기능.
import tweepy
import datetime

#관리 페이지의 컨슈머 키와 시크릿 값.
consumer_key="" #자신의 consumer_key
consumer_secret="" #자신의 consumer_secret"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)

#액세스 토큰과 시크릿 값
access_token="" #독자의 access_token
access_token_secret="" #독자의 access_token_secret

auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

#트윗 포스트하기:현재 시간과 문구를 트위터에 포스트
tweet=str(datetime.datetime.now())+'Brain Python Test.'
api.update_status(status=tweet)

print("Successfully Posted.")
print() #빈 줄 출력

#타임 라인 읽어오기:타임라인을 읽어와 cmd에 출력. 트윗한 내용을 확인할 수 있습니다.
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
