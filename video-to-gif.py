from moviepy.editor import *
# install moviepy using pip3 install moviepy

video = VideoFileClip("My_Video.mp4")
video.write_gif("My_video.gif")
