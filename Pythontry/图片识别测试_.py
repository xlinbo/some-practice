import pytesseract
import os
from PIL import Image
image_folder = "C:\\Users\\Hermite\\Desktop\\壁纸"
output_file = "C:\\Users\\Hermite\\Desktop\\Pythontry\\输出结果"
with open(output_file, 'w') as f:
    for filename in os.listdir(image_folder):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image, lang='eng')
            f.write(f'壁纸: {filename}\n')
            f.write(f'输出结果: {text}\n\n')




