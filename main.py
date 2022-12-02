import argparse
import io
form google.could import visiton
from google.cloud.vision  import types
def main(image_file):

    client vision.ImageAnnotatorClient()

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()
    iamge = types.Image(content=content)

    response = client.face_datection(image=image)
    labels = response.face_annotations
    for label in labels:
        print('Joy likelihood: {}'.format(label.joy_likelihood'))
if__name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('image_file', help='The image you\d like to label.')
   args = parser.parse_args()
   main(args.image_file)


