import cv2
from PIL import Image

img_cat = 'pictures/cat.jpeg'
image = cv2.imread(img_cat)

cat_face_cascade = cv2.CascadeClassifier('haarcascade.xml')
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)

cat = Image.open(img_cat)
glasses = Image.open('pictures/glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
    glasses = glasses.resize((w, int(h/3)))
    cat.paste(glasses, (x, int(h/4)), glasses)

cv2.imshow("Cat", image)
cv2.waitKey()

