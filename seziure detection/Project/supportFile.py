import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageOps , ImageFilter
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tf.keras.models.load_model("keras_model.h5")
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

def predict(image_path):
    # Replace this with the path to your image
    image = Image.open(image_path)

    # Resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    # Turn the image into a numpy array
    image_array = np.asarray(image)

    # Display the resized image
    # image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Run the inference
    prediction = model.predict(data)
    print(prediction)
    idx = np.argmax(prediction)

    if idx == 0:
        return "Normal EEG"
    elif idx == 1:
        return "Epileptic EEG"
    else:
        raise ValueError("Unexpected prediction index: {}".format(idx))

if __name__ == "__main__":
    result = predict("static/images/test_image.jpg")
    print(result)
