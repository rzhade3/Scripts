import praw
import csv
from datetime import datetime


count = 0


reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username = '',
                     password = '',
                     user_agent = '')


with open('Subreddit List.csv', 'r') as srlist:
    with open('Reddit Project.csv', 'w') as csvfile:
        reader = csv.reader(srlist)
        writer = csv.writer(csvfile)
        
        writer.writerow(['Title', 'Author', 'Text', 'Link', 'Date', 'Time', 'Upvotes', 'Downvotes'])
        
        for line in reader:
            if line[0] == 'Subreddit':
                continue
            
            try:
                subreddit = reddit.subreddit(line[0]) #Title of Subreddit
                print(line[0])
                for x in range(20):
                    post = subreddit.random() #Gets a random post from the current sebreddit
                    author = post.author #Gets the redditor class object of the author of the post
                    print(str(author))
                    posts = author.submissions.new() #Orders by newest to oldest                
                    for post in posts:
                        try:
                            date = datetime.fromtimestamp(post.created) 
                            if post.selftext != '':
                                count += 1
                                print(count) #Keeps track of how many have text
                            writer.writerow([post.title, str(author), post.selftext, post.url, date.date(), date.time(), post.ups, post.downs])
                        except Exception as e:
                            print(e)
            except Exception as e:
                print(e)


csvfile.close()