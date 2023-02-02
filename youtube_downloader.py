#pytube
from pytube import YouTube

#creating a variable
link = input("Enter youtube link: ")
download_video_link = YouTube(link)
title = download_video_link.title
num_of_views = download_video_link.views
lenght_of_video = download_video_link.length
author_of_video = download_video_link.author

print("Title: ", title)
print("Num_of_views: ", num_of_views)
print("length of video: ", lenght_of_video, "Seconds")
print("Author of video: ", author_of_video)

download_video_link.streams.get_highest_resolution().download()
print("Download Done")