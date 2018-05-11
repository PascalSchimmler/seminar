from moviepy.editor import *
import numpy as np
import os

vid = os.listdir(r"D:\Uni\Seminar\leecher\Ninja")
print("D:/Uni/Seminar/leecher/Ninja/" + vid[0])

string = np.array(6)

string[0] = "D:/Uni/Seminar/leecher/Ninja/" + vid[0]
#for i in range(len(vid)):
#	a = "D:/Uni/Seminar/leecher/Ninja/" + vid[i]
#	string[i] = a
	#a = ffmpeg_extract_subclip(string, 989, 999)
	#b = ffmpeg_extract_subclip(string, 1000, 1010)
	#del string