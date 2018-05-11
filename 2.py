import numpy as np
import os
import subprocess
import cv2 as cv2
import glob
from moviepy.editor import VideoFileClip
from tqdm import tqdm

#pyav
#def pyavConvertToNpArray(vidInPath, vidOutPath):
#	container = av.open(vidInPath)
#
#	for frame in container.decode(video=0):
#		frame.to_image().save((vidOutPath + 'frame-%04d.jpg') % frame.index)
#	return

# Every path of every video in directoy will be saved in string
#dirPath = "D:/Uni/Seminar/leecher/Ninja/"
def listVidsInDirWithFramerate60(dirPath):
	path = os.listdir(dirPath)
	string = ["" for x in range(len(path))]

	for i in range(len(path)):
		if getFramerate(dirPath + path[i]) == 60:
			string[i] = dirPath + path[i]
	return string

#doesnt work for some
def getFramerate(clipPath):
	con = "ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 " + clipPath
	proc = subprocess.Popen(con, stdout=subprocess.PIPE, shell=True)
	framerateString = str(proc.stdout.read())[2:-5]
	a = int(framerateString.split('/')[0])
	b = int(framerateString.split('/')[1])
	print(a,b)

	return int(np.round(np.divide(a,b))) #rounding may be counterproductive


def getFrameRateOfAll(dirPath):
	arr = listVidsInDirWithFramerate60(dirPath)
	a = np.zeros(len(arr))
	for i in  range(len(arr)):
		a[i] = np.int(getFramerate(arr[i]))

	return list(map(int, a))

def cropPartOfVideo(vidInPath, vidOutPath, out_w, out_h, x, y):
	cropCmd = 'ffmpeg -i ' + vidInPath + ' -vf \"crop=' + out_w + ':' + out_h + ':' + x + ':' + y + '\" ' + vidOutPath + " -y"
	print(cropCmd)
	subprocess.call(cropCmd)
	return
#cropPartOfVideo('D:/Uni/Seminar/leecher/Ninja/stream2.mp4', 'D:/Uni/Seminar/leecher/Ninja/testing2.mp4', '348', '80', '1600', '300')

def xFramesPerSecond(vidInPath, x, vidOutPath):
	frameCmd = 'ffmpeg -i ' + vidInPath + ' -r ' + str(x) + ' ' + vidOutPath + '%04d.mp4'
	subprocess.call(frameCmd)
	return
#xFramesPerSecond('D:/Uni/Seminar/leecher/Ninja/stream1.mp4', 1, 'D:/Uni/Seminar/leecher/Ninja/')

def cutVideo(vidInPath, vidOutPath, startTime, endTime):
	cutCmdFirst = 'ffmpeg -ss ' + startTime + ' -i ' + vidInPath + ' -c copy -t ' + endTime + ' ' + vidOutPath + ' -y'
	subprocess.call(cutCmdFirst)
	#cutCmdSecond = 'ffmpeg -ss 30 -i ' + tmp + ' -c copy -t 10 ' + vidOutPath
	#subprocess.call(cutCmdSecond)
	return

#this one sucks
def blackedOut(vidInPat, vidOutPath):
	#blackCmd = 'ffmpeg -i ' + vidInPat + ' -vf hue=s=0 -c:a copy ' + vidOutPath
	blackCmd = 'ffmpeg -y -i ' + vidInPat + ' -f avi ' + vidOutPath
	subprocess.call(blackCmd)
	return
#blackedOut('D:/Uni/Seminar/leecher/Ninja/stream1.mp4', 'D:/Uni/Seminar/leecher/Ninja/black2.avi')

def videoToImageSequence(vidInPath, vidOutPath):
	conv = 'ffmpeg -i ' + vidInPath + ' -vf fps=1 ' + vidOutPath + 'video-frame%05d.png'
	subprocess.call(conv)
	return
videoToImageSequence('D:/Uni/Seminar/leecher/Ninja/stream2.mp4', 'D:/Uni/Seminar/leecher/Ninja/stream2/')

def arrayFromBMP(dirPath):
	X_data = []
	files = glob.glob(dirPath + '*.BMP')

	for myFile in files:
		image = cv2.imread(myFile)
		X_data.append(image)

	print(len(X_data))
	print('X_data shape:', np.array(X_data).shape)

def mp4FromBmpSequence(dirPath, vidOutPath):
	seq = 'ffmpeg -i ' + dirPath + ' -pix_fmt yuv420p -y ' + vidOutPath
	subprocess.call(seq)

	return
mp4FromBmpSequence('D:/Uni/Seminar/leecher/Ninja/faster/video-frame%05d.png', 'D:/Uni/Seminar/leecher/Ninja/faster.mp4')

#arrayFromBMP('D:/Uni/Seminar/leecher/Ninja/blackbump/')
#xFramesPerSecond('D:/Uni/Seminar/leecher/Ninja/black2.mp4', 1, 'D:/Uni/Seminar/leecher/Ninja/blackbump/')
#cutVideo('D:/Uni/Seminar/leecher/Ninja/stream1.mp4', 'D:/Uni/Seminar/leecher/Ninja/cut2.mp4', '00:40:00', '00:00:50')
#cropPartOfVideo('D:/Uni/Seminar/leecher/Ninja/kek.mp4', 'D:/Uni/Seminar/leecher/Ninja/kek2.mp4', '350', '300', '1600', '300')
#cropPartOfVideo('D:/Uni/Seminar/leecher/Ninja/kek.mp4', 'D:/Uni/Seminar/leecher/Ninja/kek2.mp4', '348', '80', '1', '1')
#blackedOut('D:/Uni/Seminar/leecher/Ninja/kek2.mp4', 'D:/Uni/Seminar/leecher/Ninja/black2.mp4')
#print("Framerate of Videos in D:/Uni/Seminar/leecher/Ninja/: ", getFrameRataeOfAll('D:/Uni/Seminar/leecher/Ninja/'))

#def fitInto30or60Fps(clip)
#a = getFramerate(listVidsInDir("D:/Uni/Seminar/leecher/Ninja/")[0])
#print(a)

