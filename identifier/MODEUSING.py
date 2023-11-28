# Predict from web - this is an image of Titian.
# Replace 'url' with any image of one of the 11 artists above and run this cell.
# Prediction
from keras.preprocessing import *
from keras.models import load_model
from skimage.io import imread
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import imageio.v2 as imageio
import cv2

# artists = pd.read_csv('input/artists.csv')
# artists.shape
# images_dir = 'input/images/images'
# # Sort artists by number of paintings
# artists = artists.sort_values(by=['paintings'], ascending=False)

# # Create a dataframe with artists having more than 200 paintings
# artists_top = artists[artists['paintings'] >= 200].reset_index()
# artists_top = artists_top[['name', 'paintings']]
# #artists_top['class_weight'] = max(artists_top.paintings)/artists_top.paintings
# artists_top['class_weight'] = artists_top.paintings.sum() / (artists_top.shape[0] * artists_top.paintings)

# artists_top_name = artists_top['name'].str.replace(' ', '_').values

# batch_size = 16
# train_input_shape = (224, 224, 3)
# n_classes = artists_top.shape[0]

# train_datagen = ImageDataGenerator(validation_split=0.2,
#                                    rescale=1./255.,
#                                    #rotation_range=45,
#                                    #width_shift_range=0.5,
#                                    #height_shift_range=0.5,
#                                    shear_range=5,
#                                    #zoom_range=0.7,
#                                    horizontal_flip=True,
#                                    vertical_flip=True,
#                                   )
# train_generator = train_datagen.flow_from_directory(directory=images_dir,
#                                                     class_mode='categorical',
#                                                     target_size=train_input_shape[0:2],
#                                                     batch_size=batch_size,
#                                                     subset="training",
#                                                     shuffle=True,
#                                                     classes=artists_top_name.tolist()
#                                                    )
# labels = train_generator.class_indices
# labels = dict((v,k) for k,v in labels.items())

labels = {0: 'Vincent_van_Gogh', 1: 'Edgar_Degas', 2: 'Pablo_Picasso', 3: 'Pierre-Auguste_Renoir', 4: 'Albrecht_Dürer', 5: 'Paul_Gauguin', 6: 'Francisco_Goya', 7: 'Rembrandt', 8: 'Alfred_Sisley', 9: 'Titian', 10: 'Marc_Chagall'}
print(labels)
loaded_model = load_model('identifier/keras_model.h5')
model = loaded_model
import imageio
import cv2
train_input_shape = (224, 224, 3)
random_image_file = ("identifier/Pablo_Picasso_4.jpg")
web_image = imageio.imread(random_image_file)
web_image = cv2.resize(web_image, dsize=train_input_shape[0:2], )
web_image = image.img_to_array(web_image)
web_image /= 255.
web_image = np.expand_dims(web_image, axis=0)


prediction = model.predict(web_image)
prediction_probability = np.amax(prediction)
prediction_idx = np.argmax(prediction)

print(labels)
print("Predicted artist =", labels[prediction_idx].replace('_', ' '))
print("Prediction probability =", prediction_probability*100, "%")

plt.imshow(imageio.imread(random_image_file))
plt.axis('off')
plt.show()