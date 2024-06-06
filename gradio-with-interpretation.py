import gradio as gr
import tensorflow as tf
from tensorflow.keras.applications import ResNet50, resnet50
from tensorflow.keras.applications.resnet50 import decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

print(gr.__version__)

# Load the pre-trained ResNet50 model
model = ResNet50(weights="imagenet")


# Define the prediction function
def predict(img):
    img = img.resize((224, 224))  # Resize image to fit model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = resnet50.preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded_preds = decode_predictions(preds, top=3)[0]

    return {label: float(score) for (_, label, score) in decoded_preds}


# Define the interpretation function
def interpret(img):
    img = img.resize((224, 224))  # Resize image to fit model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = resnet50.preprocess_input(img_array)

    with tf.GradientTape() as tape:
        tape.watch(img_array)
        preds = model(img_array)
        top_pred_index = tf.argmax(preds[0])
        top_class_channel = preds[:, top_pred_index]

    grads = tape.gradient(top_class_channel, img_array)[0]
    saliency = tf.reduce_max(tf.abs(grads), axis=-1)
    saliency = np.maximum(saliency, 0)
    saliency = (saliency / saliency.max()).numpy()

    return saliency


interface = gr.Interface(
    fn=predict,
    inputs=gr.Image('PIL'),
    outputs=gr.Label(num_top_classes=1)
)

interface.interpret(interpret)

# Launch the interface
interface.launch()