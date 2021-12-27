import os
import cv2
import base64
import urllib.request
from .darknet_release.darknet import darknet_pic


def get_pic(url):
    print('-----------------------------------------')
    raw_file_name = 'rawPic.png'
    new_file_name = 'newPic.png'

    print('>> Reading {}'.format(url))
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with open(raw_file_name, 'wb') as f:
        with urllib.request.urlopen(req) as r:
            f.write(r.read())

    print('>> Processing {}'.format(raw_file_name))
    # img = cv2.imread(raw_file_name)
    # h, w, _ = img.shape
    # img = cv2.rectangle(img,
    #                     (int(w*0.5), int(h*0.5)),
    #                     (int(w*0.7), int(h*0.7)),
    #                     color=(255, 255, 255),
    #                     thickness=3,
    #                     )
    # cv2.imwrite(new_file_name, img)

    darknet_pic(raw_file_name, new_file_name)

    print('>> New file is generated {}'.format(new_file_name))
    print('-----------------------------------------')
    image_buffer = b''
    with open(new_file_name, 'rb') as f:
        image_buffer = base64.b64encode(f.read()).decode('utf-8')

    return image_buffer
