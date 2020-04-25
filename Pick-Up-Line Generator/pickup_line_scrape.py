import praw
reddit = praw.Reddit(client_id='QXeIVRnwCi17Tw',
                     client_secret='Lbo_78FkdTLvoUSfqaAv0_HgzxA',
                     user_agent='reddit_scrape')

hot_posts = reddit.subreddit('pickuplines').hot(limit=10000)
f= open("pick_up_lines.txt","w+", encoding="utf-8")
i=0
for post in hot_posts:
    i=i+1
    print(post.title)
    print(i)
    f.write(post.title +" "+"<|endoftext|>\n")
