import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from scipy import misc
import h5py
import Image

# ----------- rgb to grayscale ----------------
def rgb2grey(rgb):
	'''
	convert an rgb image to a grayscale image
	'''
	return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

# ----------- pairing images ------------------
def pairingImg(img1Path, img2Path, onWidth):
	'''
	combine a pair of images horizontally or vertically
	'''
	if onWidth:
		imgLeft = misc.imread(img1Path)
		imgRight = misc.imread(img2Path)
		if imgLeft.shape[0] != imgRight.shape[1]:
			raise Exception("Two images do not have the same height!")
		return np.insert(imgLeft, imgRight, axis=1)
	else:
		imgUp = misc.imread(img1Path)
		imgDown = misc.imread(img2Path)
		if imgUp.shape[1] != imgDown.shape[1]:
			raise Exception("Two images do not have the same width!")
		return np.insert(imgUp, imgDown, axis=0)

# ---------- store images in hdf5 ------------
def writeImg2DB(hdf5Name, d, datasetName):
	'''
	hdf5Name: hdf5 file name
	d: data
	datasetName: dataset name 
	'''
	h5f = h5py.File(hdf5Name, "w")
	h5f.create_dataset(datasetName, data=d)
	h5f.close()

# ---------- read images from hdf5 -----------
def readImgFromDB(hdf5Name, datasetName):
	'''
	hdf5Name: hdf5 file name
	datasetName: dataset name
	'''
	h5f = h5py.File(hdf5Name, "r")
	imagergbd2 = h5f[datasetName][:]
	h5f.close()
	return imagergbd2	

# ---------- recover the image matrix --------
print imagergbd2 == imagergbd

# ---------- combine hdf5 files on hard drive 

# ----------- read images into matrix ---------
image = misc.imread('sample.png')

#imaged = misc.imread('sampled.png')
imaged = np.asarray(Image.open("sampled.png").convert("L"))

#print image.shape
#print image.shape[0]
#print image.shape[1]
#print imaged.shape

# ----------- merge rgb and d --------------
def mergrgbd(imagergb, imaged):
	'''
	add depth to rgb
	'''
	imagergbd = np.insert(image, 3, imaged, axis=2)
	return imagergbd

#for i in range(image.shape[0]):
#	for j in range(image.shape[1]):
#		image[i][j].append(imaged[i][j])

#print image
#print imaged
#print sum(imaged)
print imagergbd
print imagergbd.shape



#plt.imshow(imaged)
#plt.show()

plt.imshow(imaged, cmap=cm.Greys_r)
plt.show()


