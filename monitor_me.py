#!/usr/bin/env python
#coding: UTF-8
import subprocess
import datetime
import tweepy
import const

#認証取得
auth = tweepy.OAuthHandler(const.CONSUMER_KEY, const.CONSUMER_SECRET)
auth.set_access_token(const.ACCESS_TOKEN, const.ACCESS_SECRET)
api = tweepy.API(auth)

#現在日時で写真を撮影
now = datetime.datetime.now()
fileName =  '/home/pi/images/' + \
    now.strftime('%Y%m%d_%H%M%S') + '.jpg'
cmd = 'raspistill -w 800 -h 600 -o ' + fileName
subprocess.call(cmd, shell=True)

api.update_with_media(status = str(now) + ' #RaspberryPi', filename = fileName)

subprocess.call('rm ' + fileName, shell=True)
