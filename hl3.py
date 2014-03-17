import praw
from time import sleep
import re

#login

r = praw.Reddit(user_agent='hl3_confirmer_bot by u/sallurocks version 1.0')
r.login('Enter User Name','Enter Password')



#work on getting /r gaming comments


#subreddit = r.get_subreddit('gaming')
#flat_comments = subreddit.get_comments()



condition = True
msg="Thank you For Confirming Half-Life 3,Your Outstanding Logical And Mathematical Skills Will Forever Be Remembered.\n\n\nYour Confirmation Is Being Confirmed For Future Reference\n\n______________________________\n\nCurrent Confirmation Count:"
keyword={'hl3 confirmed','hl3 confirm','hl confirm','hl 3 confirm','hl confirmed','hl 3 confirmed','half life confirm','half life 3 confirm','half-life 3 confirmed','halflife3 confirmed','half life3 confirm','half-life3 confirm'}

while condition:

    #a+ to append everytime
    fo=open("test.txt","a+")
    f1=open("count.txt","r+")

    count=f1.read()
    count=int(count)

    #to read the entire file and check id to prevent duplicate posts
    #need to seek pointer to the beginning and put it back at the end
    position=fo.tell()
    fo.seek(0,0)
    str=fo.read()
    fo.seek(position)


    #submissions = r.get_submission(submission_id='1z6x8s')
    #flat_comments = praw.helpers.flatten_tree(submissions.comments)
    subreddit = r.get_subreddit('gaming+dota2+steam+HalfLife')
    flat_comments = subreddit.get_comments()

    for comment in flat_comments:
        for value in keyword:
            
            if( ( value in comment.body.lower() ) and (comment.id not in str)):

                print('Ok!')
                print(comment.body)
                count=count+1
                comment.reply(msg+"%s" % count)
                fo.write(comment.id+" ")
                f1.seek(0,0)
                f1.write("%s" % count)
    
            else:
                print("No")
                print(comment.body)
            

    fo.close()
    f1.close()
    sleep(5)
    


