import PIL.Image as Image
import glob
from tqdm import tqdm
list = glob.glob('D:/Uni/Seminar/leecher/Ninja/benchmark/*.png')

image_list = []
i = 0
for filename in glob.glob('name_of_folder/*.jpg'):
	if(i == 5000):
		break
	im=Image.open(filename)
	image_list.append(im)

a=0
c=[]
for i in range(0,len(image_list)):
	c.crop.crop((0,470,400,720))
	c.append(image_list[i])
	c[i].save()


i = 0
for path in tqdm(list):
	img = Image.open(path)
	face = img.crop((0,470,400,720))
	face.save('D:/Uni/Seminar/leecher/Ninja/benchmark/face/face' + str(i) + '.png')
	number = img.crop((1622,300,1900,350))
	number.save('D:/Uni/Seminar/leecher/Ninja/benchmark/number/number' + str(i) + '.png')
	i = i+1
