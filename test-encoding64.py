import base64

with open("deer.gif", "rb") as image:
  image_read = image.read()
  image_64_encode = base64.encodebytes(image_read)

image_64_decode = base64.decodebytes(image_64_encode)
with open("deer_decode.gif", "wb") as image_result:
  image_result.write(image_64_decode)
