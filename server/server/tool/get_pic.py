import os
import cv2
import base64
import urllib.request
from pathlib import Path
from .darknet_release.darknet import darknet_pic


def mk_buffer(path):
    path = Path(path)

    image_buffer = b''
    with open(path, 'rb') as f:
        image_buffer = base64.b64encode(f.read()).decode('utf-8')

    ext = path.suffix[1:]
    buffer = 'data:image/{};base64,{}'.format(ext, image_buffer)
    return buffer, ext


def get_pic(url):
    print('-----------------------------------------')
    suffix = '.' + url.split('.')[-1]
    ext = '.png'
    # if suffix in ['.jpg']:
    #     ext = suffix

    raw_file_name = 'rawPic' + suffix
    new_file_name = 'newPic.png'

    print('>> Reading {}'.format(url))
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with open(raw_file_name, 'wb') as f:
        with urllib.request.urlopen(req) as r:
            content = r.read()
            f.write(content)

    # img = cv2.imread(raw_file_name)
    # cv2.imwrite(raw_file_name, img)

    print('>> Processing {}'.format(raw_file_name))
    darknet_pic(raw_file_name, new_file_name)
    print('>> New file is generated {}'.format(new_file_name))

    image_buffer, ext = mk_buffer(new_file_name)

    print('-----------------------------------------')
    return image_buffer, ext
