from PIL import Image
import os

def convert_to_grayscale(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endwith(".gif"):
            img = Image.open(filename)
            converted_img = img.convert('L').resize((200,200))
            converted_img.save(output_dir+'\gs_'+filename)
