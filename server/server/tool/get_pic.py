import os
import cv2
import base64
import urllib.request
from pathlib import Path
from .darknet_release.darknet import darknet_pic


def mk_base64(path):
    path = Path(path)

    # !!! The code is NOT for this function,
    # !!! but it is used for return a picture thought the server.
    # with open(path, 'rb') as f:
    #     return f.read(), 'jpg'

    image_buffer = b''
    with open(path, 'rb') as f:
        image_buffer = base64.b64encode(f.read()).decode('utf-8')

    ext = path.suffix[1:]
    buffer = 'data:image/{};base64,{}'.format(ext, image_buffer)
    return buffer, ext


def get_pic(url, method, WallHaven_DIR):
    print('-----------------------------------------')
    raw_file_name = 'rawPic.png'
    new_file_name = 'newPic.png'

    if method == 'URL':
        print('>> Reading URL {}'.format(url))
        req = urllib.request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        with open(raw_file_name, 'wb') as f:
            with urllib.request.urlopen(req) as r:
                content = r.read()
                f.write(content)

    if method == 'Thumb':
        print('>> Reading Thumb: {}'.format(url))
        raw_file_name = str(WallHaven_DIR.joinpath(
            'assets/_thumb').joinpath(url))

    if method == 'FullSize':
        print('>> Reading FullSize: {}'.format(url))
        raw_file_name = str(WallHaven_DIR.joinpath(
            'assets/_fullSize').joinpath(url))

    # img = cv2.imread(raw_file_name)
    # cv2.imwrite(raw_file_name, img)

    print('>> Processing {}'.format(raw_file_name))
    darknet_pic(raw_file_name, new_file_name)
    print('>> New file is generated {}'.format(new_file_name))

    image_buffer, ext = mk_base64(new_file_name)

    print('-----------------------------------------')
    return image_buffer, ext
