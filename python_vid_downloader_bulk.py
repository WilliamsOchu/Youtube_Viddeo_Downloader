#!/usr/bin/env python3

## We will write this script to be able to download a bulk of videos from YouTube

## Firstly lets import the necessary modules

from pytube import YouTube

## Lets instantiate a variable to hold our video links

video_list =[]
video_links = input("Paste your video links separated by a space: ")
video_links = video_links.split(' ') 
for ind_link in video_links:
    video_list.append(ind_link)
    
print('\n')

## Lets get a location to store our downloaded videos
download_location = input("Enter a location to where videos will be saved: ")
print('\n')

## Lets proceed to load the videos to be downloaded
for each_video in video_list:
    each_video = YouTube(each_video)
    each_video = each_video.streams.get_highest_resolution()
    
    try:
        print('Download in progress  ...... \n')
        each_video.download(download_location)
    except:
        print('Error !! .. Unable to download video')
    print('Download Complete .....  {}'.format(each_video.title))
    
    