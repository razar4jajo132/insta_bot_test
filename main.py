# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:58:53 2023

@author: razar
"""

import instaloader as insta
from instaloader import Hashtag,TopSearchResults
import os
import time

path = r'C:\\Users\\razar\\InstaPy\\assets\\gecko\\v0.32.0\\geckodriver-v0.32.0-win64\\geckodriver.exe'
test = open(path, "r")


user = 'the_budgeting_babe'
passwd = 'eS8P-kN^FLrpRC.'

from instapy import InstaPy
from instapy import smart_run
# login credentials
insta_username = user  # <- enter username here
insta_password = passwd  # <- enter password here
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,password=insta_password,headless_browser=False)
session.login()
time.sleep(5)

test.close

#%%

def insta_like(user,passwd):
    
# imports
    from instapy import InstaPy
    from instapy import smart_run
    # login credentials
    insta_username = user  # <- enter username here
    insta_password = passwd  # <- enter password here
    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False)
    with smart_run(session):
        """ Activity flow """
        # general settings
        #sets the percentage of people you want to follow
        session.set_do_follow(True, percentage=50)
        #sets the percentage of posts you want to comment
        session.set_do_comment(True, percentage=100)
        #list of random comments you want to post
        session.set_comments(["hey @_.interwined_dodos._, have a look", "Great content @_.interwined_dodos._ have a look", ":heart_eyes: :heart_eyes: :heart_eyes: @_.interwined_dodos._"])
        #setting quotas for the daily and hourly action(I said it's smart)
        session.set_quota_supervisor(enabled=True, peak_comments_daily=250, peak_comments_hourly=30, peak_likes_daily=250, peak_likes_hourly=30,sleep_after=['likes', 'follows'])
        #again some set of configuration which figures out whom to follow
        session.set_relationship_bounds(enabled=True,
                                        delimit_by_numbers=True,
                                        max_followers=4590,
                                        min_followers=45,
                                        min_following=77)
        #tags to get posts from and amout is the actions you want 
        session.like_by_tags(['nailsofinstagram',"nails"], amount=300)
    return()

i=0
os.getcwd()
os.chdir(r'C:\Users\razar\OneDrive\Documents\Insta_Upload\Download\test_down')
L = insta.Instaloader()


tot = 5         #number of loops

choose = 0
# L.login(user, passwd)

# for post in insta.Hashtag.from_name(L.context, 'Finance').get_posts():
#     # post is an instance of instaloader.Post
#     L.download_post(post, target='#Finance')
hashtag = Hashtag.from_name(L.context,'finance')
search = TopSearchResults(L.context, 'finance budget')
if choose == 1:
    for post in hashtag.get_posts():
       print(post)
       print(i)
       L.download_post(post, target="#"+hashtag.name)
       if i == tot:
           break
       else:
           pass
       i=i+1
else:
    for post in search.get_profiles():
       print(post)
       print(i)
       # L.download_post(post, target=)
       if i == tot:
           break
       else:
           pass
       i=i+1
   
   
   
   
   
   
   
   
   
