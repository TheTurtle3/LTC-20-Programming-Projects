from PIL import Image

def resize_image(s1, s2):
    image = Image.open('Image resize/test.jpg')
    print(f"Current size:  {image.size}")

    resized_image = image.resize((s1,s2))
    resized_image.save('Image resize/resized-test.jpg')

s1 = int(input('Enter Width: '))
s2 = int(input('Enter Height: '))
resize_image(s1,s2)