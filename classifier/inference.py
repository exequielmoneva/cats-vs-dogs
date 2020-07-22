import os

import numpy as np
import tensorflow as tf

SIZE = 150
CLASSES = ['Cat', 'Dog']
export_path = os.path.join(os.getcwd(), 'model')
stra = "classifier/model"
model = tf.keras.models.load_model(stra)


def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE, SIZE)
    )
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    response = model.predict(image)
    prediction = np.squeeze(response)
    class_name = CLASSES[int(prediction > 0.5)]
    return class_name
