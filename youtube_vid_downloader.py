#!/usr/bin/env python3

from pytube import YouTube

## lets denote the link of the youtube video we want to download 
video_link = input("Paste the link to your video: ")
print('\n')

## Lets instantiate a directory where the video will be saved
video_location = input("Enter a directory to store your videos: ")
print('\n')

## Lets open up the video as an object
to_be_download = YouTube(video_link)

## Lets get a very decent resolution for the video 
to_be_download = to_be_download.streams.get_highest_resolution()

## Lets try to download the video if there is a working network connection
try: 
    print('Download in progress...... \n')
    to_be_download.download(video_location)
    
except:
    print("An Error has occured")
print('Download Succesful .....  {}'.format(to_be_download.title))
