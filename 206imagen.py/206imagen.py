from PIL import Image, ImageFilter

img=Image.open('img1.png')

filtered_img=img.convert('L')

filtered_img.save('grey.png')

#crojk=filtered_img.rotate(90)

resize=filtered_img.resize((100,100))

resize.save('grey1.png')

#crojk.save('grey.png','png')

print(img)

