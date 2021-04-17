from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing import image
import sys
import numpy as np

files = sys.argv[1:]

net_final = load_model('./models/model-resnet50-final.h5')

cls_list = ['ok', 'thumb']

#f = "./test_images/thumb/frame_01_05_0005.png"
f = "./test_images/ok/frame_06_07_0009.png"

img = image.load_img(f, target_size=(180, 180))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)
pred = net_final.predict(x)[0]
top_inds = pred.argsort()[::-1][:5]
print(f)
print(top_inds)
for i in top_inds:
    print('{:.3f}  {}'.format(pred[i], cls_list[i]))