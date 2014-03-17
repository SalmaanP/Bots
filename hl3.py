import praw
from time import sleep

#login

r = praw.Reddit(user_agent='example')
r.login('bottestbot','bottestbot')



#work on getting /r gaming comments


#subreddit = r.get_subreddit('gaming')
#flat_comments = subreddit.get_comments()





while True:

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
    subreddit = r.get_subreddit('BOTTESTBOT')
    flat_comments = subreddit.get_comments()
    for comment in flat_comments:
        if(('HL3 confirmed' in comment.body) and (comment.id not in str)):
            print('Ok!')
            print(comment.body)
            count=count+1
            comment.reply("Alright Noted count:%s" % count)
            fo.write(comment.id+" ")
            f1.seek(0,0)
            f1.write("%s" % count)
            
        else:
            print("No")
            print(comment.body)
            sleep(30)

    fo.close()
    f1.close()
    


