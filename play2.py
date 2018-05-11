import PIL.Image as Image
import glob
from tqdm import tqdm
list = glob.glob('D:/Uni/Seminar/leecher/Ninja/20180430_256154372_Fortnite/*.png')

i = 0
for path in tqdm(list):
	img = Image.open(path)
	face = img.crop((0,470,400,720))
	face.save('D:/Uni/Seminar/leecher/Ninja/20180430_256154372_Fortnite/face/face' + str(i) + '.png')
	number = img.crop((1622,300,1900,350))
	number.save('D:/Uni/Seminar/leecher/Ninja/20180430_256154372_Fortnite/number/number' + str(i) + '.png')
	i = i+1
