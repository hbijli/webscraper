from william_sonoma.images import *
from william_sonoma.calculator import basic_calculator
from william_sonoma.web_scraper import *

###### Basic Calculator Tests
assert basic_calculator('2+3*6') == 20
assert basic_calculator('-1+1') == 0
assert basic_calculator('1+0') == 1
assert basic_calculator('-0+0') == 0
assert basic_calculator('(5+3)*4/5') == 6.4
assert basic_calculator('999999999999999999') == 999999999999999999
assert basic_calculator('2)3') == 'Error'
assert basic_calculator('sdsds') == 'Error'


##### Web scraper tests
url1 = 'https://www.google.com'
url2 = 'https://kraken.com'

#1 Google returns only one image.
assert len(return_image_urls(url1)) == 1

#2 kraken returns multiple images. Atleast one image should return
assert len(return_image_urls(url1)) > 0

#3 Validate if urls returned are images
for item in return_image_urls(url2):
    assert item[-4:] == '.png' or item[-4:] == '.jpg' or item[-4:] == '.gif' or item[-5:] == '.jpeg'

##### Image tests

# Adjust path
image_input_dir = 'E:\Test\william_sonoma\images'
image_output_dir = 'E:\Test\william_sonoma\images-gs'
convert_to_grayscale(image_input_dir, image_output_dir)

#1 Test directory is not empty
assert len(os.listdir(image_output_dir)) > 0

#2 Test image is grayscale and size is (200 x 200)
for filename in os.listdir(image_output_dir):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endwith(".gif"):
        img = Image.open(filename)
        assert img.mode == 'L'
        assert img.size == (200, 200)
