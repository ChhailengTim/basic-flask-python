from PIL import Image


def resize_image(size1,size2):
    image = Image.open('cat.jpg')

    print(image.size)

    resize_image =  image.resize((size1, size2))

    print(resize_image.size)

    resize_image.save('new50'+ str(size1) +'.jpg')

z1 = int(input("Input your size1: "))
z2 = int(input("Input your size2: "))
resize_image(z1, z2)
