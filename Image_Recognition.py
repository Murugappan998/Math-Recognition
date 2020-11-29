import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
def solution(f_path):
    img = Image.open(f_path)
    text = tess.image_to_string(img)
    text = text.split()
    for i in text:
        pass
    try:    
        return eval(i)
    except:
        return "Image is not recognisable"