import numpy as np
from skimage.io import imread
from skimage.transform import resize

#util layers
def img_preprocess(img_path):
    mean = [103.939, 116.779, 123.68]
    img = imread(img_path)
    img = resize(img, (224, 224))*255.0
    if len(img.shape) == 2:
        img = np.dstack([img,img,img])
    img[:,:,0] -= mean[2]
    img[:,:,1] -= mean[1]
    img[:,:,2] -= mean[0]
    img[:,:,[0,1,2]] = img[:,:,[2,1,0]]
    img = np.reshape(img,[1,224,224,3])
    return img
