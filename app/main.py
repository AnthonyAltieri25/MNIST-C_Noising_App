import numpy as np
import streamlit as st
from PIL import Image
import io

def random_noise_corruption(arr, input_strength = .5):
    '''Adds noise based on random distribution'''
    arr = np.divide(arr.astype('float32'), 255)
    arr += (input_strength * np.random.normal(loc=0.0, scale=.5, size=arr.shape))
    arr = np.clip(arr, 0.0, 1.0)

    arr = np.multiply(arr, 255)
    arr = arr.astype('uint8')
    print("\rRANDOM CORRUPTION COMPLETE")
    return arr


buffer = io.BytesIO()

st.title("SURP2023 MNIST-C Image Noiser")

#Get the image from user
user_file = st.file_uploader("Enter an MNIST-C image", type=['jpg', 'png'], accept_multiple_files=False)

while(user_file is None):
    pass

st.write("Image received")

#Get image
image = Image.open(user_file)
#Get pixel values in array
arr = np.array(image)

#Corrupt the image pixel values and make a new image object from the array
image = Image.fromarray(obj=random_noise_corruption(arr))
image.save(buffer, format='PNG')

#Give the user button to download data
st.download_button(label='Download Noised Image', data=buffer, file_name='Noised.png')















