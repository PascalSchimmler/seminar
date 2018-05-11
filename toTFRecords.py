import PIL.Image as Image
import glob
from tqdm import tqdm
from io import StringIO
import tensorflow as tf
import subprocess
from io import BytesIO
import datetime
glob.glob(r'D:\Uni\Seminar\leecher\Ninja\faster\*.png')

import os

def _bytes_feature(value):
	return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _int64_feature(value):
	return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

#tfrDir: D:/Uni/Seminar/leecher/Ninja/record.tfrecords
#pngdir: r'D:\Uni\Seminar\leecher\Ninja\faster\*.png'
def pngImagesToTfrecords(pngDir, tfrDir):
	#options = tf.python_io.TFRecordOptions(tf.python_io.TFRecordCompressionType.GZIP)
	#writer = tf.python_io.TFRecordWriter(tfrDir , options=options)
	writer = tf.python_io.TFRecordWriter(tfrDir)

	imagesPath = pngDir
	addrs = glob.glob(imagesPath) #puts the imagePaths in one memorychunk

	for i in tqdm(range(addrs.__len__())):
		img =open(addrs[i], 'rb').read()
		#height = img.shape[0]
		#width = img.shape[1]

		#img_raw = img.tostring()

		example = tf.train.Example(features=tf.train.Features(feature={
		#'height': _int64_feature(height),
		#'width': _int64_feature(width),
		'image_raw': _bytes_feature(img)}))

		#dataset = tf.data.TFRecordDataset(filenames=filenames, compression_type='GZIP', buffer_size=buffer_size)

		writer.write(example.SerializeToString())

	writer.close()

#pngImagesToTfrecords(r'D:\Uni\Seminar\leecher\Ninja\faster\*.png', r'D:\Uni\Seminar\leecher\Ninja\record.tfrecords')

#r'D:\Uni\Seminar\leecher\Ninja\record.tfrecords'
def reconstruct(tfrDir):
	reconstructed_images = []

	#options = tf.python_io.TFRecordOptions(tf.python_io.TFRecordCompressionType.GZIP)
	#record_iterator = tf.python_io.tf_record_iterator(path=tfrDir, options=options)

	record_iterator = tf.python_io.tf_record_iterator(path=tfrDir)

	for string_record in tqdm(record_iterator):
		example = tf.train.Example()
		example.ParseFromString(string_record)

		#height = int(example.features.feature['height']
		#			 .int64_list
		#			 .value[0])

		#width = int(example.features.feature['width']
		#			.int64_list
		#			.value[0])

		img_raw = (example.features.feature['image_raw']
			.bytes_list
			.value[0])

		reconstructed_images.append(img_raw)
	return reconstructed_images

def videoToImageSequence(vidInPath, vidOutPath):
	conv = 'ffmpeg -i ' + vidInPath + ' -vf fps=1 ' + vidOutPath + 'video-frame%05d.png'
	subprocess.call(conv)
	return

#needs 10 minutes per hour
def cropVideo(vidInPath, vidOutPath):
	crop = 'ffmpeg -i ' + vidInPath + ' -filter_complex "[0:v]crop=400:200:0:484[face];[0:v]crop=300:50:1624:300[number]" -map [face] -map 0:a ' + vidOutPath + '/face/face.mp4 -map [number] -map 0:a ' + vidOutPath + '/number/number.mp4'
	subprocess.call(crop)
	return

#~1,2 minutes per hour
def justDoThis(name):
	videoToImageSequence('D:/Uni/Seminar/leecher/Ninja/'+name+'/face.mp4', 'D:/Uni/Seminar/leecher/Ninja/'+name+'/face/')
	videoToImageSequence('D:/Uni/Seminar/leecher/Ninja/'+name+'/number.mp4', 'D:/Uni/Seminar/leecher/Ninja/'+name+'/number/')
	#cropVideo('D:/Uni/Seminar/leecher/Ninja/'+name+'.mp4', 'D:/Uni/Seminar/leecher/Ninja/'+name+'/')

	#pngImagesToTfrecords('D:/Uni/Seminar/leecher/Ninja/'+name+'/*.png', 'D:/Uni/Seminar/leecher/Ninja/'+name+'Record.tfrecords')
	#re = reconstruct('D:/Uni/Seminar/leecher/Ninja/'+name+'Record.tfrecords')
	#a = Image.open(BytesIO(re[0])).show()
	#a.save('D:/Uni/Seminar/leecher/Ninja/heartless.png')
	return

print(datetime.datetime.time(datetime.datetime.now()))
#justDoThis('benchmarkTest')
print(datetime.datetime.time(datetime.datetime.now()))

#dirPath = 'D:/Uni/Seminar/leecher/Ninja/'
def preprocessAllInDir(dirPath):
	vids = glob.glob(dirPath + '*.mp4')

	for video in tqdm(vids):
		a = str(os.path.basename(video)).split('.')[0]
		#print('Makedir: ' + dirPath + a)
		#print('Makedir: ' + dirPath + a + '/face')
		#print('Makedir: ' + dirPath + a + '/number')
		#print('cropVideo: ' + dirPath + a + '.mp4' + ' | ' + dirPath + a + '/')
	if not os.path.exists(dirPath + a):
			os.makedirs(dirPath + a)
			os.makedirs(dirPath + a + '/face')
			os.makedirs(dirPath + a + '/number')
			os.makedirs(dirPath + a + '/number/visible')
			os.makedirs(dirPath + a + '/number/invisible')
			cropVideo(dirPath + a + '.mp4', dirPath + a + '/')
			videoToImageSequence(dirPath + a + '/face/face.mp4', dirPath + a + '/face/')
			videoToImageSequence(dirPath + a + '/number/number.mp4', dirPath + a + '/number/')
	return
preprocessAllInDir('D:/Uni/Seminar/leecher/Ninja/')