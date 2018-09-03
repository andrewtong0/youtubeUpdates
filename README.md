# youtubeUpdates
Pushes updates to the console when a new YouTube video from a specified channel is released

## Dependencies
* URL Requests (for pulling the HTML feed data)
* Beautiful Soup (for parsing the HTML data)
* Time (for delaying subsequent URL calls)

## What It Does
youtubeUpdates will push a message to the console when a new YouTube video is uploaded from a user. Can be easily converted to notifications through another medium (e.g. Discord/Slack)

## Necessary Input
In order to make the code work, you must modify the following in the code:
* Input the list of channels as their associated RSS feeds in the list variable "youtubeChannels"
  * To create a YouTube RSS feed, take the channel ID of the desired channel and paste it after "https://www.youtube.com/feeds/videos.xml?channel_id=".
    * e.g. if your channel ID is 1234abc: "https://www.youtube.com/feeds/videos.xml?channel_id=1234abc"
  * A channel ID can be found by going to a YouTube channel and copying the URL after /channel/ and should look like a random string of characters
    * e.g. Mark Rober's channel link is "https://www.youtube.com/channel/UCY1kMZp36IQSyNx_9h4mpCg", so his channel ID is UCY1kMZp36IQSyNx_9h4mpCg

## Important Notes
* If a user uploads more than one video before the next call is made, it will only show the latest video
* If a user uploads two videos in a row with the exact same name, it will not update (since the name of the video is used to check whether a new video goes up)
