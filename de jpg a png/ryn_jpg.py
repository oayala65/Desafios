import sys
import os
from PIL import Image

image_folder=sys.argv[1]
out_folder=sys.argv[2]

#print(image_folder,out_folder)

if not os.path.exists(out_folder):
    os.makedirs(out_folder)

for filename in os.listdir(image_folder):

    img=Image.open(f'{image_folder}{filename}')
    
    clean_name=os.path.splitext(filename)[0]
    
    img.save(f'{out_folder}{clean_name}.png', 'png')
    
    print('all done')

# DESDE LA TERMINAL....
# SE EJECUTA ASÍ:    python ryn_jpg.py fotos/ convert/
# fotos/ es un directorio en donde estan los archivos que van a ser convertidos
# convert/ es el diretorio a donde van los archivos convertidos.