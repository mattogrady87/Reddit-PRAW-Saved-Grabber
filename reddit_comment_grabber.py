import praw
import comment_config
from time import localtime, strftime
import os




def bot_login():
    print("Logging in...")
    r = praw.Reddit(client_id = comment_config.client_id,
                    client_secret = comment_config.client_secret,
                    password = comment_config.password,
                    username = comment_config.username,
                    user_agent = "Comment Grabber!")
    print("Logged in!")
    return r

r = bot_login()
multi = r.multireddit('ragnar_graybeard87', '0x01myitmulti').subreddits
sub_dict = {}

    
for x in r.redditor('ragnar_graybeard87').saved(limit=None):
    if x.subreddit_name_prefixed[2:] in multi:
        sub_dict[x] = x.created

sorted_list = sorted(sub_dict, key=sub_dict.get,
                         reverse=True)

for x in sorted_list:
    if 'comment' in x.__doc__:
        print(strftime('%m-%d-%Y', localtime(x.created)))
        print(x.link_title)
        print(x.link_url)
        print(x.subreddit_name_prefixed)
        print("\n\n")

    else:
        print(strftime('%m-%d-%Y', localtime(x.created)))
        print(x.title)
        print(x.url)
        print(x.subreddit_name_prefixed)
        print("\n\n")
