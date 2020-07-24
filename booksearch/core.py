import imghdr
import pathlib
from .api import get_data, get_json

class Book:

    def __init__(self, item):
        self.id = item['id']
        volume_info = item['volumeInfo']
        for k, v in volume_info.items():
            setattr(self, str(k), v)

    def __repr__(self):
        return str(self.__dict__)

    def save_thumbnails(self, prefix):
        paths = []
        for kind, url in self.imageLinks.items():
            thumbnail = get_data(url)

            ext = imghdr.what(None, h=thumbnail)

            base = pathlib.Path(prefix) / f'{self.id}_{kind}'
            filename = base.with_suffix(f'.{ext}')
            filename.write_bytes(thumbnail)
            paths.append(filename)
        return paths

def get_books(q, **params):
    params['q'] = q
    data = get_json(params)
    return [Book(item) for item in data['items']]