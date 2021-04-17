import tensorflow as tf
import pathlib
from tensorflow import keras
import numpy as np
import logging
tf.get_logger().setLevel(logging.ERROR)
import json

for x in range(10):
    #class_names = ["ok","thumb"]
    class_names = ['c', 'five', 'four', 'l', 'ok', 'one', 'palm', 'three', 'thumb', 'two']
    img_height = 180
    img_width = 180
    model = tf.keras.models.load_model('models/basic_neural')
    test_file_path = "./test_images"
    test_file_path = pathlib.Path(test_file_path)
    thumb_test_file_path = "./test_images/gesture.png"

    img = keras.preprocessing.image.load_img(
        thumb_test_file_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    gesture = format(class_names[np.argmax(score)])
    #print(gesture)
    confident = format(100 * np.max(score))
    #print(confident)

    """
    score_result = {}
    score_result['result'] = []
    score_result['result'].append({
        'gesture': gesture,
        'confident': confident
    })
    """

    score_result = {
    'gesture': gesture,
    'confident': confident
    }

    with open('./score_result/result.json', 'w') as json_file:
        json.dump(score_result, json_file)

