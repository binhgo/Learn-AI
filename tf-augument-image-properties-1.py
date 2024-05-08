import tensorflow as tf


def augument_image(image):
    image = tf.keras.utils.img_to_array(image)
    image = tf.image.random_brightness(image=image, max_delta=0.25)
    image = tf.image.random_contrast(image, 0.5, 2.0)
    image = tf.image.random_saturation(image, 0.75, 1.25)
    image = tf.image.random_hue(image, 0.1)
    image = tf.transpose(image, (2, 0, 1))
    return image


def transform(image):
    image = tf.keras.utils.img_to_array(image)
    image = tf.transpose(image, (2, 0, 1))
    return image
