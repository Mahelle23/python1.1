import pytesseract
import re
from PIL import Image

#set up the tesseract ocr engine
pytesseract.pytesseract.tesseract_cmd=r'c:/program files/tesseract-OCR/tesseract'

# define the path to the to the image file
image_file = "E:\python1.1\EIcWiYEo.jpg"

#open the image file using the pillow library
img = Image.open(image_file)

#extract text from the image using Tessseract ocr
text = pytesseract.image_to_string(img, lang='eng')

#use regular expressions to search for the person's full name in the extracted text 
match = re.search(r'\b([A-Z][a-z]+)\s([A-Z][a-z]+)\b', text)

if match:
    full_name = match.group(0)
    print("found the person's full name", full_name)
else:
    print("did not find the person's full name in the image") 