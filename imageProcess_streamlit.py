## -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 12:00:00 2022

@author: jpstaub for Ripcord Engineering and Active House USA

Image processing utility for Velux Daylight Visualizer zone images.

1. Removes Daylight Factor scale from image.
2. Makes Daylight Factor image with transparent background.
3. Crops Daylight Factor image with transparent background.
4. Saves cropped Daylight Factor image with transparent background for use.

Saved images can be underlayed and scaled on background plans to give
architectural context to Daylight Factor results.
"""

# streamlit on PyPi: https://pypi.org/project/xgbxml/
# opencv-python on PyPi: https://pypi.org/project/opencv-python/#description

# import packages
import cv2
import numpy as np
import streamlit as st
from io import BytesIO
import zipfile



# upload files
def upload_files():
    print("Uploaded image files.")

# filter file
def filter_file(file):
    if('w_zone' in file.name.split('.')[0]):
        return True    

# make image from file object
# https://stackoverflow.com/questions/47515243/reading-image-file-file-storage-object-using-opencv
def make_image(file):
    filestr = file.read()
    file_bytes = np.fromstring(filestr, np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    return img

# crop out daylight factor scale
def remove_scale(img):
    img = img[0:800, 200:1446]
    return img

# make grayscale image with cvtColor() function
def make_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

# make mask image with threshold() function
def make_mask(img):
    msk = cv2.threshold(img, 15, 255, cv2.THRESH_BINARY)[1]
    return msk

# make transparent background image by placing the mask into the alpha channel
def make_transparent(img, msk):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img[:, :, 3] = msk
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    return img 
    
# get bounding rectangle of mask shape (should be one around the nonzero pixels)
def get_bounding(msk):
    contours = cv2.findContours(msk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    contour = contours[0]
    x,y,w,h = cv2.boundingRect(contour)
    return x,y,w,h

# crop image with bounding rectangle
def crop_image(img,x,y,w,h):
    img = img[y:y+h, x:x+w]
    return img

# make caption
def make_caption(file):
    caption = file.name.split('.')[0] + '_crop.' + file.name.split('.')[-1]
    return caption

# save cropped image
def write_image(file,img):
    filename = file.name.split('.')[0] + '_crop.' + file.name.split('.')[-1]
    image_file = cv2.imwrite(filename, img)
    return image_file

# encode image
def encode_image(file,img):
    extension = '.' + file.name.split('.')[-1]
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    img_encode = cv2.imencode(extension, img)[1]
    data_encode = np.array(img_encode)
    byte_encode = data_encode.tobytes()
    return byte_encode

# make zip archive
# https://www.neilgrogan.com/py-bin-zip/
def generate_zip(files):
    mem_zip = BytesIO()
    
    with zipfile.ZipFile(mem_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zf: 
        for f in files:
            zf.writestr(f[0], f[1])
    return mem_zip.getvalue()

                         
# streamlit application
# front matter
title_body = '[VDV Report Image Processor](https://github.com/jpstaub/imageProcess_streamlit)'
sub_body = 'by [Active House USA](https://activehouseusa.org/)'

st.title(title_body)
st.subheader(sub_body)


# upload images
upload_files_label = 'Velux Daylight Visualizer Report Images'
upload_files = st.sidebar.file_uploader(upload_files_label, type = ['jpg','png'], accept_multiple_files=True, on_change = upload_files())
if not upload_files:
    st.stop()
    

# make cropped images
crop_files = []
for upload_file in upload_files:
    if filter_file(upload_file):
        # st.write(upload_file)
        original_image = make_image(upload_file)
        # st.image(original_image, channels='BGR')
        image = remove_scale(original_image)
        gray = make_gray(image)
        mask = make_mask(gray)
        new_img = make_transparent(image, mask)            
        try:
            x,y,w,h = get_bounding(mask)
        except IndexError:
            msg_error = 'The following file has no image to process: ' + upload_file.name
            st.write(msg_error)
        else:
            crop = crop_image(new_img, x,y,w,h)
            # show cropped images
            st.image(crop, caption=make_caption(upload_file), output_format='PNG')
            # make list of encoded cropped images
            crop_files.append((make_caption(upload_file), encode_image(upload_file, crop)))            
            

# present results
msg_success = 'Image processing complete!'
st.sidebar.success(msg_success)

full_zip_in_memory = generate_zip(crop_files)

st.sidebar.download_button(
    label='Download processed images',
    data=full_zip_in_memory,
    file_name='processed_images.zip',
    mime='application/zip')

