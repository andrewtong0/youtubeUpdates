from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

# Insert the channels you would like to check as a list here
# Must be in the RSS feed format (https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID_HERE)
# e.g. Mark Rober's channel ID = UCY1kMZp36IQSyNx_9h4mpCg, input as below
youtubeChannels = ['https://www.youtube.com/feeds/videos.xml?channel_id=UCY1kMZp36IQSyNx_9h4mpCg']
# Dictionary with key as channel RSS feed link, value is the latest video title; used to check if a new video with a different name comes up
latestVideosDict = {}
counter = 0
listCounter = 0
previous_video = ""
timer = 0

# Initialize the latestVideos dictionary with empty strings
for x in youtubeChannels:
    latestVideosDict[youtubeChannels[listCounter]] = ''
    listCounter += 1

while(1 == 1):
    counter = 0

    for x in youtubeChannels:
        url_page = x
        html_page = urlopen(url_page)
        soup = BeautifulSoup(html_page, 'html.parser')
        entry = soup.find('entry')
        latest_video = entry.find('title').get_text()
        latest_video_link = str(entry.find('link')).partition('href="')[2].partition('" rel')[0]
        
        # If the latest video doesn't match what is stored, must be a new video; update dictionary, print to console
        if latestVideosDict[youtubeChannels[counter]] != latest_video:
            latestVideosDict[youtubeChannels[counter]] = latest_video
            print(latest_video)
            print(latest_video_link)
        counter += 1
        
    # Delay between subsequent calls
    time.sleep(10)
    timer = timer + 10
    print('Pass: ' + str(timer/10))
