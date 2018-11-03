import webbrowser
import random


season = random.randint(1,22)

#14 episode seasons
if season in [5,8,9,10,11,12,13,14,15,16]: 
    episode = random.randint(1,14)
#10 episode seasons
elif season in [17,18,19,20,21,22]: 
    episode = random.randint(1,10)
#17 episode seasons
elif season in [3,4,6]:
    episode = random.randint(1,17)
#13 episode seasons
elif season == 1:
    episode = random.randint(1,13)
#18 episode seasons
elif season == 2:
    episode = random.randint(1,18)
#15 episode seasons
elif season == 7:
    episode = random.randint(1,15)

#convert ints to strings for url 
if season < 10:
    season = "0"+str(season)
else:
    season = str(season)
if episode < 10:
    episode = "0"+str(episode)
else:
    episode = str(episode)

url = "http://southpark.cc.com/full-episodes/s" + season + "e" + episode
webbrowser.open(url)


