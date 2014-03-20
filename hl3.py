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
msg="Thank you for confirming Half-Life 3, your outstanding logical and mathematical skills will forever be remembered.\n\n\nYour confirmation is being confirmed for future reference\n\n______________________________\n\nCurrent confirmation count:"
keyword={'hl3 confirmed','hl3 confirm','hl confirm','hl 3 confirm','hl confirmed','hl 3 confirmed','half life confirm','half life 3 confirm','half-life 3 confirmed','halflife3 confirmed','half life3 confirm','half-life3 confirm','hl3 is confirmed','half life 3 is confirmed','half-life 3 is confirmed','hl 3 is confirmed','half life 3 - confirmed'}

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
    subreddit = r.get_subreddit('dota2+steam+gaming+halflife+globaloffensive')
    flat_comments = subreddit.get_comments()
    try:
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
                    break;
                    
           
                else:
                    print("No")
                    print(comment.body)

    except KeyboardInterrupt:
        running = False
    except praw.errors.APIException as e:
        print("[ERROR]:", e)
        print("sleeping 300 sec")
        sleep(300)
    except Exception as e: # In reality you don't want to just catch everything like this, but this is toy code.
        print("[ERROR]:", e)
        print("blindly handling error")
        continue 
            
            

    fo.close()
    f1.close()
    sleep(20)
    


